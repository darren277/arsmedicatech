"""
LiveKit Video Recording
"""
import asyncio
import os
import time
from typing import Any, Dict, Tuple

import boto3  # type: ignore[import-untyped]
import requests  # type: ignore[import-untyped]
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from livekit import api  # type: ignore

API_KEY    = os.environ["LIVEKIT_API_KEY"]
API_SECRET = os.environ["LIVEKIT_API_SECRET"]
SERVER_URL = os.environ.get("LIVEKIT_URL", "https://your-livekit-domain")

app = Flask(__name__)

CORS(
    app,
    supports_credentials=True,
    origins=["http://localhost:3000", "http://localhost:3012"],
)

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

    tok = api.AccessToken(API_KEY, API_SECRET).with_identity(identity).with_grants(api.VideoGrants(room_join=True, room=room)).to_jwt() # type: ignore[call-arg]

    return jsonify(token=tok), 200

# ---- 2.  start / stop composite recording ----
@app.post("/video/start-recording")
def start_recording() -> Tuple[Response, int]:
    """
    Start a composite recording for a specific room.
    :return: A tuple with the egress ID and HTTP status code 200.
    """
    body: Dict[str, Any] = request.get_json() or {}
    room: str = body["room"]

    filename = f"recordings/{room}-{int(time.time())}.mp4"

    # Setup request
    s3_output = api.EncodedFileOutput(
        filepath=filename,
        s3=api.S3Upload(
            bucket=os.environ["LIVEKIT_S3_BUCKET"],
        )
    )
    request_obj = api.StartEgressRequest(
        room_name=room,
        file_outputs=[s3_output],
        layout="speaker",
    )

    # Run async LiveKit API call from sync Flask route
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        info = loop.run_until_complete(api.egress.start_egress(request_obj))
        egress_id = info.egress_id
        return jsonify(egress_id=egress_id), 200
    finally:
        loop.run_until_complete(api.aclose())
        loop.close()

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
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(api.egress.stop_egress(api.StopEgressRequest(
            egress_id=egress_id
        )))
        return "", 204
    finally:
        loop.run_until_complete(api.aclose())
        loop.close()

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

        # Handle event types
        if event["event"] == "egress_ended":
            location = event.get("file", {}).get("location", "")
            print("✅ Recording stored at:", location)

        elif event["event"] == "room_finished":
            print(f"Room {event.get('room', {}).get('name')} finished")

        # Add more event types if needed

        return "ok", 200
    except Exception as e:
        print(f"⚠️ Webhook verification failed: {e}")
        return "unauthorized", 401

if __name__ == "__main__":
    app.run(port=5001, debug=True)
