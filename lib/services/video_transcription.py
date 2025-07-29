"""
Video transcription Celery task service.
"""
import os, tempfile, subprocess, pathlib

import boto3 # type: ignore
# or minio

import whisper # type: ignore

from celery import shared_task # type: ignore
from settings import logger

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT_URL", "https://s3.amazonaws.com"),
    aws_access_key_id=os.getenv("S3_ACCESS_KEY_ID", "your-access-key"),
    aws_secret_key=os.getenv("S3_ACCESS_KEY_ID", "your-access-key"),
    region_name=os.getenv("S3_REGION_NAME", "us-east-1"),
)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def transcribe_video_task(self, s3_uri: str, room: str, duration: float):
    """
    1. Download mp4 from S3/MinIO
    2. Extract audio (ffmpeg) → wav
    3. Run Whisper → text
    4. Upload .txt to transcripts/ bucket/key.txt
    """
    bucket, key = s3_uri.replace("s3://", "").split("/", 1)

    with tempfile.TemporaryDirectory() as tmpdir:
        mp4_path = f"{tmpdir}/video.mp4"
        wav_path = f"{tmpdir}/audio.wav"
        txt_path = f"{tmpdir}/transcript.txt"

        # 1. download
        s3.download_file(bucket, key, mp4_path)

        # 2. ffmpeg – 16 kHz mono wav (Whisper likes 16- or 32-bit PCM)
        subprocess.run(
            ["ffmpeg", "-nostdin", "-i", mp4_path,
             "-ar", "16000", "-ac", "1", "-f", "wav", wav_path],
            check=True,
        )

        # 3. whisper
        model = whisper.load_model(os.getenv("WHISPER_MODEL", "base.en"))
        result = model.transcribe(wav_path)
        with open(txt_path, "w") as f:
            f.write(result["text"])

        # 4. upload
        out_bucket = os.getenv("TRANSCRIPT_BUCKET", bucket)
        out_key    = key.replace("recordings/", "transcripts/").rsplit(".", 1)[0] + ".txt"
        s3.upload_file(txt_path, out_bucket, out_key)

        return {"out": f"s3://{out_bucket}/{out_key}", "duration": duration}
