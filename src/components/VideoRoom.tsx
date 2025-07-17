import {
  ControlBar,
  GridLayout,
  LiveKitRoom,
  ParticipantTile,
  RoomAudioRenderer,
  useTracks,
} from '@livekit/components-react';
import '@livekit/components-styles';
import { Track } from 'livekit-client';
import { useEffect, useState } from 'react';
import { LIVE_KIT_SERVER_URL } from '../env_vars';
import { videoAPI } from '../services/api';

export default function VideoRoom() {
  const [token, setToken] = useState<string>();
  const roomName = 'demo-room';
  const identity = 'alice';
  // fetch a fresh JWT from Flask
  useEffect(() => {
    // The AbortController is used to cancel the request if the component unmounts.
    const controller = new AbortController();

    const fetchToken = async () => {
      try {
        const r = await videoAPI.getToken(
          roomName,
          identity,
          controller.signal
        );
        setToken(r.token);
      } catch (error) {
        // If the request was aborted, we can safely ignore the error.
        if (controller.signal.aborted) {
          console.log('Token fetch was aborted.');
          return;
        }
        console.error('Failed to fetch token:', error);
      }
    };

    fetchToken();

    // The cleanup function aborts the fetch request on unmount.
    return () => {
      controller.abort();
    };
  }, []); // Empty dependency array is correct here since roomName and identity are static.

  // A more explicit loading state
  if (token === '') {
    return <div>Getting token...</div>;
  }

  return (
    <LiveKitRoom
      token={token}
      serverUrl={LIVE_KIT_SERVER_URL}
      data-lk-theme="default"
      style={{ height: '100vh' }}
      // For a better experience we can handle disconnects
      onDisconnected={() => console.log('Disconnected from room')}
    >
      <MyVideoConference />
      <RoomAudioRenderer />
      <ControlBar>
        <button onClick={() => videoAPI.startRecording(roomName)}>
          Start Recording
        </button>
        <button onClick={() => videoAPI.stopRecording('your-egress-id-here')}>
          Stop Recording
        </button>
      </ControlBar>
    </LiveKitRoom>
  );
}

function MyVideoConference() {
  const tracks = useTracks([
    { source: Track.Source.Camera, withPlaceholder: true },
    { source: Track.Source.ScreenShare, withPlaceholder: true },
  ]);
  return (
    <GridLayout tracks={tracks}>
      <ParticipantTile />
    </GridLayout>
  );
}
