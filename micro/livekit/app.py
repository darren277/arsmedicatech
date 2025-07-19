"""
LiveKit Video Recording
"""
from concurrent.futures import ThreadPoolExecutor

import asyncio
import os
import time
from typing import Any, Dict, Tuple

from celery import Celery

import boto3  # type: ignore[import-untyped]
import requests  # type: ignore[import-untyped]
from flask import Flask, Response, jsonify, request
from flask_cors import CORS # type: ignore[import-untyped]
from livekit import api  # type: ignore


celery_app = Celery(
    "producer",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND")
)


API_KEY    = os.environ["LIVEKIT_API_KEY"]
API_SECRET = os.environ["LIVEKIT_API_SECRET"]
SERVER_URL = os.environ.get("LIVEKIT_URL", "https://your-livekit-domain")

executor = ThreadPoolExecutor()


app = Flask(__name__)

CORS(
    app,
    supports_credentials=True,
    origins=["http://localhost:3000", "http://localhost:3012"],
)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---- 1.  mint join tokens ----
@app.post("/livekit/token")
def create_token() -> Tuple[Response, int]:
    """
    Create a LiveKit join token for a specific room and identity.
    :return: A JSON response containing the token.
    """
    body: Dict[str, Any] = request.json or {}
    room: str = body["room"]
    identity: str = body["identity"]

    tok = api.AccessToken(API_KEY, API_SECRET).with_identity(identity).with_grants(api.VideoGrants(room_join=True, room=room)).to_jwt() # type: ignore[call-arg]

    return jsonify(token=tok), 200

# ---- 2.  start / stop composite recording ----
from livekit.protocol.egress import EgressInfo, RoomCompositeEgressRequest, EncodedFileOutput, S3Upload # type: ignore[import-untyped]

@app.post("/livekit/start-recording")
def start_recording() -> Tuple[Response, int]:
    """
    Start a composite recording for a specific room.
    :return: A tuple with the egress ID and HTTP status code 200.
    """
    body: Dict[str, Any] = request.get_json() or {}
    room: str = body["room"]

    filename = f"recordings/{room}-{int(time.time())}.mp4"

    logger.info(f"Starting recording for room: {room}, filename: {filename}")

    async def run() -> EgressInfo:
        """
        Create a LiveKit API client and start egress recording.
        :return: EgressInfo object containing egress details.
        """
        lk_api = api.LiveKitAPI(  # This returns an object with `.egress` and `.aclose()`
            url=SERVER_URL,
            api_key=API_KEY,
            api_secret=API_SECRET,
        )
        try:
            logger.info(f"Creating egress for room: {room}, filename: {filename}")
            logger.info(f'Using S3 bucket: {os.environ["LIVEKIT_S3_BUCKET"]}, access_key: {os.environ["LIVEKIT_S3_ACCESS_KEY"]}, secret_key: {os.environ["LIVEKIT_S3_SECRET_KEY"]}')
            request_obj = RoomCompositeEgressRequest(
                room_name=room,
                file_outputs=[
                    EncodedFileOutput(
                        filepath=filename,
                        s3=S3Upload(
                            bucket=os.environ["LIVEKIT_S3_BUCKET"],
                            access_key=os.environ["LIVEKIT_S3_ACCESS_KEY"],
                            secret=os.environ["LIVEKIT_S3_SECRET_KEY"],
                            region=os.environ.get("LIVEKIT_S3_REGION", "us-east-1"),
                        )
                    )
                ],
                layout="speaker",
            )
            info = await lk_api.egress.start_room_composite_egress(request_obj)
            logger.info(f"Egress Info: {info}")
            logger.info(f"Recording started with egress ID: {info.egress_id}")
            #return jsonify(egress_id=info.egress_id), 200
            return info.egress_id  # Return the EgressInfo object
        finally:
            await lk_api.aclose()  # Ensure the API client is closed properly

    # Run async LiveKit API call from sync Flask route
    def blocking_call() -> str:
        """
        Create a LiveKit API client and start egress recording in a blocking manner.
        :return: The egress ID as a string.
        """
        return asyncio.run(run())

    future = executor.submit(blocking_call)
    egress_id = future.result()

    return jsonify({"egress_id": egress_id}), 200


@app.post("/livekit/stop-recording")
def stop_recording() -> Tuple[Response, int]:
    """
    Stop an ongoing egress recording.
    :return: A tuple with an empty string and HTTP status code 204.
    """
    body: Dict[str, Any] = request.get_json() or {}
    egress_id: str = body.get("egress_id", "")
    logger.info(f"Stopping recording with egress ID: {egress_id}")
    if not egress_id:
        return jsonify({"message": "Missing egress_id"}), 400

    async def run() -> None:
        """
        Create a LiveKit API client and stop the egress recording.
        :return: None
        """
        lk_api = api.LiveKitAPI(
            url=SERVER_URL,
            api_key=API_KEY,
            api_secret=API_SECRET,
        )
        try:
            await lk_api.egress.stop_egress(
                api.StopEgressRequest(egress_id=egress_id)
            )
        except api.twirp_client.TwirpError as te:
            # Ignore if the egress is already finished/failed
            if te.code in ("not_found", "failed_precondition"):
                pass
            else:
                raise
        except Exception as e:
            logger.info(f"⚠️ Error stopping egress: {e}")
            raise
        finally:
            await lk_api.aclose()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def blocking_stop() -> None:
        """
        Create a LiveKit API client and stop the egress recording in a blocking manner.
        :return: None
        """
        logger.info(f"Stopping egress with ID: {egress_id}")
        return asyncio.run(run())

    # Submit async call in background thread
    future = executor.submit(blocking_stop)
    future.result()

    return jsonify({"message": "recording stopped"}), 200


# ---- 3.  receive webhooks (room finished, egress finished, etc.) ----
from livekit.api import TokenVerifier, WebhookReceiver  # type: ignore

verifier = TokenVerifier(
    api_key=API_KEY,
    api_secret=API_SECRET,
)
receiver = WebhookReceiver(verifier)

@app.post("/livekit/webhook")
def webhook() -> Tuple[str, int]:
    """
    Receive LiveKit webhooks.
    :return: "ok" if successful, or an error message.
    """
    try:
        # Decode and verify the webhook event
        auth_header = request.headers.get("Authorization", "")
        event = receiver.receive(request.data.decode(), auth_header)

        logger.info(f"📦 Incoming webhook event: {event}")

        # Handle event types
        if event.event == "egress_ended":
            egress_info = event.egress_info
            location = getattr(egress_info.file, "filename", "")
            room = getattr(egress_info, "room_name", "")
            duration = int((getattr(egress_info, "ended_at", 0) - getattr(egress_info, "started_at", 0)) / 1e9)

            if not location:
                logger.info("⚠️ No file location found in event")
                return "no file location", 400
            if not room:
                logger.info("⚠️ No room name found in event")
                return "no room name", 400
            if duration <= 0:
                logger.info("⚠️ Invalid duration in event")
                return "invalid duration", 400

            # Kick off async transcription
            #transcribe_video_task.delay(location, room, duration)
            celery_app.send_task(
                "lib.services.video_transcription.transcribe_video_task",
                args=(location, room, duration),
            )
            logger.info(f"✅ Recording stored at: {location} (room: {room}, duration: {duration}s)")

        elif event.event == "room_finished":
            room_info = event.room
            room_name = room_info.name if room_info else "unknown"
            logger.info(f"Room finished: {room_name}")

        # Add more event types if needed

        return "ok", 200
    except Exception as e:
        logger.info(f"⚠️ Webhook verification failed: {e}")
        return "unauthorized", 401

if __name__ == "__main__":
    app.run(port=5001, debug=True)
