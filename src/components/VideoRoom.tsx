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
import { LIVE_KIT_SERVER_URL } from '../env_vars';
import { videoAPI } from '../services/api';
import logger from '../services/logging';

export default function VideoRoom() {
  const [token, setToken] = useState<string>();
  const roomName = 'demo-room';
  const identity = 'alice';

  useEffect(() => {
    // fetch a fresh JWT from Flask
    videoAPI.getToken(roomName, identity).then(r => {
      logger.debug('token', JSON.stringify(r));
      setToken(r.token);
    });
  }, []);

  if (!token) return <p>loading...</p>;

  return (
    <LiveKitRoom
      token={token}
      serverUrl={LIVE_KIT_SERVER_URL}
      data-lk-theme="default"
      style={{ height: '100vh' }}
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
  const tracks = useTracks([{ source: 'camera' }, { source: 'screen_share' }]);
  return (
    <GridLayout tracks={tracks}>
      <ParticipantTile />
    </GridLayout>
  );
}
