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
import { useUser } from './UserContext';

function MyCustomControls({ roomName }: { roomName: string }) {
  const [egressId, setEgressId] = useState<string | null>(null);

  const handleStart = async () => {
    try {
      const res = await videoAPI.startRecording(roomName);
      console.log('Started recording with ID:', res.egress_id);
      setEgressId(res.egress_id);
    } catch (e) {
      console.error('Start recording failed', e);
    }
  };

  const handleStop = async () => {
    try {
      if (egressId) {
        await videoAPI.stopRecording(egressId);
        console.log('Stopped recording with ID:', egressId);
        setEgressId(null);
      }
    } catch (e) {
      console.error('Stop recording failed', e);
    }
  };

  return (
    <div style={{ position: 'relative' }}>
      <ControlBar />

      <div
        style={{
          position: 'absolute',
          bottom: '4rem', // Adjust depending on the bar height
          left: '50%',
          transform: 'translateX(-50%)',
          display: 'flex',
          gap: '1rem',
          zIndex: 1000,
        }}
      >
        <button
          onClick={handleStart}
          style={{ padding: '0.5rem 1rem', fontSize: '1rem' }}
        >
          Start Recording
        </button>
        <button
          onClick={handleStop}
          disabled={!egressId}
          style={{ padding: '0.5rem 1rem', fontSize: '1rem' }}
        >
          Stop Recording
        </button>
      </div>
    </div>
  );
}

export default function VideoRoom() {
  const { user, isAuthenticated } = useUser();
  const [identity, setIdentity] = useState<string>();

  const [token, setToken] = useState<string>();

  //const roomName = 'demo-room';
  const roomName = window.location.pathname.split('/').pop() || 'default-room';

  // fetch a fresh JWT from Flask
  useEffect(() => {
    // The AbortController is used to cancel the request if the component unmounts.
    const controller = new AbortController();

    if (isAuthenticated && user) {
      setIdentity(user.username);
    } else {
      setIdentity('guest-' + Math.random().toString(36).substring(2, 15));
    }

    const fetchToken = async (identity: string) => {
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

    identity && fetchToken(identity);

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
      style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}
      // For a better experience we can handle disconnects
      onDisconnected={() => console.log('Disconnected from room')}
    >
      <div style={{ flex: 1, position: 'relative' }}>
        <MyVideoConference />
        <RoomAudioRenderer />
      </div>
      <MyCustomControls roomName={roomName} />
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
