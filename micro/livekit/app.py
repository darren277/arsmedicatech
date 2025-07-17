"""
LiveKit Video Recording
"""
import os
import time
from datetime import timedelta
from typing import Any, Dict, Tuple

import boto3  # type: ignore[import-untyped]
import requests
from flask import Flask, Response, jsonify, request
from livekit.api import AccessToken  # type: ignore[import-not-found]
from livekit.api import EgressClient, VideoGrant
from livekit.api.egress import (  # type: ignore[import-not-found]
    EncodedFileOutput, S3Upload)

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
    body: Dict[str, Any] = request.json or {}
    room: str = body["room"]
    identity: str = body["identity"]

    token: AccessToken = AccessToken(API_KEY, API_SECRET, identity=identity)
    token.add_grants([VideoGrant(room_join=True, room=room)])
    token.ttl = int(timedelta(hours=2).total_seconds())
    tok: str = token.to_jwt()
    return jsonify(token=tok), 200

# ---- 2.  start / stop composite recording ----
egress: EgressClient = EgressClient(SERVER_URL, API_KEY, API_SECRET)

@app.post("/video/start-recording")
def start_recording() -> Tuple[Response, int]:
    """
    Start a composite recording for a specific room.
    :return: A tuple with the egress ID and HTTP status code 200.
    """
    body: Dict[str, Any] = request.get_json() or {}
    room: str = body["room"]

    file_output: EncodedFileOutput = EncodedFileOutput(
        filepath=f"recordings/{room}-{int(time.time())}.mp4",
        output=S3Upload(bucket=os.environ["LIVEKIT_RECORDING_BUCKET"])
    )
    info = egress.start_room_composite(
        room_name=room, file_outputs=[file_output], layout="speaker"
    )
    egress_id: str = str(getattr(info, "egress_id", ""))
    return jsonify(egress_id=egress_id), 200

@app.post("/video/stop-recording")
def stop_recording() -> Tuple[str, int]:
    """
    Stop an ongoing egress recording.
    :return: A tuple with an empty string and HTTP status code 204.
    """
    body: Dict[str, Any] = request.get_json() or {}
    egress_id: str = body.get("egress_id", "")
    if not egress_id:
        return "Missing egress_id", 400
    egress.stop_egress(egress_id)
    return "", 204

# ---- 3.  receive webhooks (room finished, egress finished, etc.) ----
from livekit.api import TokenVerifier, WebhookReceiver

verifier: TokenVerifier = TokenVerifier(API_KEY, API_SECRET)
receiver: WebhookReceiver = WebhookReceiver(verifier)

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
