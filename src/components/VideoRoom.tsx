import {
  ControlBar,
  GridLayout,
  LiveKitRoom,
  ParticipantTile,
  RoomAudioRenderer,
  useTracks,
} from '@livekit/components-react';
import '@livekit/components-styles';
import { useEffect, useState } from 'react';
import { videoAPI } from '../services/api';

export default function VideoRoom() {
  const [token, setToken] = useState<string>();
  const roomName = 'demo-room';
  const identity = 'alice';

  useEffect(() => {
    // fetch a fresh JWT from Flask
    videoAPI.getToken(roomName, identity).then(r => setToken(r.token));
  }, []);

  if (!token) return <p>loading...</p>;

  return (
    <LiveKitRoom
      token={token}
      serverUrl="wss://your-livekit-domain"
      data-lk-theme="default"
      style={{ height: '100vh' }}
    >
      <MyVideoConference />
      <RoomAudioRenderer />
      <ControlBar>
        <button
          onClick={() =>
            axios.post('/video/start-recording', { room: roomName })
          }
        >
          Start Recording
        </button>
        <button
          onClick={() =>
            axios.post('/video/stop-recording', {
              // provide the correct egress_id here
              egress_id: undefined,
            })
          }
        >
          Stop Recording
        </button>
      </ControlBar>
    </LiveKitRoom>
  );
}

function MyVideoConference() {
  const tracks = useTracks([{ source: 'camera' }, { source: 'screen_share' }]);
  return (
    <GridLayout tracks={tracks}>
      <ParticipantTile />
    </GridLayout>
  );
}
