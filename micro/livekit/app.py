"""
LiveKit Video Recording
"""
import os
import time
from datetime import timedelta
from typing import Any, Dict, Tuple

import boto3
import requests
from flask import Flask, Response, jsonify, request
from livekit.api import AccessToken, EgressClient, VideoGrant
from livekit.api.egress import EncodedFileOutput, S3Upload

API_KEY    = os.environ["LIVEKIT_API_KEY"]
API_SECRET = os.environ["LIVEKIT_API_SECRET"]
SERVER_URL = os.environ.get("LIVEKIT_URL", "https://your-livekit-domain")

app = Flask(__name__)

# ---- 1.  mint join tokens ----
@app.post("/video/token")
def create_token() -> Tuple[Response, int]:
    """
    Create a LiveKit join token for a specific room and identity.
    :return: A JSON response containing the token.
    """
    body: Dict[str, Any] = request.json
    room: str = body["room"]
    identity: str = body["identity"]

    tok: str = (
        AccessToken(API_KEY, API_SECRET)
        .with_identity(identity)
        .with_grants(VideoGrant(room_join=True, room=room))
        .set_valid_for(timedelta(hours=2))
        .to_jwt()
    )
    return jsonify(token=tok), 200

# ---- 2.  start / stop composite recording ----
egress = EgressClient(SERVER_URL, API_KEY, API_SECRET)

@app.post("/video/start-recording")
def start_recording() -> Tuple[Response, int]:
    """
    Start a composite recording for a specific room.
    :return: A tuple with the egress ID and HTTP status code 200.
    """
    room: str = request.json["room"]

    file_output: EncodedFileOutput = EncodedFileOutput(
        filepath=f"recordings/{room}-{int(time.time())}.mp4",
        output=S3Upload(bucket=os.environ["LIVEKIT_RECORDING_BUCKET"])
    )
    info: Any = egress.start_room_composite_egress(
        room, file=file_output, layout="speaker"
    )
    return jsonify(egress_id=info.egress_id), 200

@app.post("/video/stop-recording")
def stop_recording() -> Tuple[str, int]:
    """
    Stop an ongoing egress recording.
    :return: A tuple with an empty string and HTTP status code 204.
    """
    egress_id: str = request.json["egress_id"]
    egress.stop_egress(egress_id)
    return "", 204

# ---- 3.  receive webhooks (room finished, egress finished, etc.) ----
from livekit.api import TokenVerifier, WebhookReceiver

verifier = TokenVerifier(API_KEY, API_SECRET)
receiver = WebhookReceiver(verifier)

@app.post("/livekit/webhook")
def webhook() -> str:
    """
    Receive LiveKit webhooks.
    :return: "ok" if successful, or an error message.
    """
    event: Dict[str, Any] = receiver.receive(request.data.decode(), request.headers["Authorization"])
    if event["event"] == "egress_ended":
        print("Recording stored at", event["file"]["location"])  # s3://...
    return "ok"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
