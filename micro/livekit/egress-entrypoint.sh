#!/bin/sh
set -e

# Set runtime dir if needed
export XDG_RUNTIME_DIR="/run/pulse"
mkdir -p "$XDG_RUNTIME_DIR"
chown -R "$(whoami)" "$XDG_RUNTIME_DIR" # Adjust user if needed

# Cleanup stale PulseAudio sockets and files if they exist
rm -rf "$XDG_RUNTIME_DIR"/pulse*
rm -f /home/egress/.config/pulse/*.tdb
rm -f /home/egress/.config/pulse/cookie
rm -f /home/egress/.pulse-cookie

# Optional: kill lingering PulseAudio processes (useful during development)
if pgrep pulseaudio > /dev/null; then
  echo "Killing existing PulseAudio process..."
  pkill pulseaudio
  sleep 1
fi

# Start PulseAudio
echo "Starting PulseAudio..."
pulseaudio --daemonize=no --log-level=debug --exit-idle-time=-1 &

# Give PulseAudio a moment to start
sleep 2

# Start LiveKit egress
#exec /usr/local/bin/egress --config /etc/livekit/egress.yaml
exec egress --config /egress.yaml
