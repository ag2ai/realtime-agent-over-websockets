
// Create an instance of AudioPlayer with the WebSocket URL
const audio = new ag2client.WebsocketAudio(socketUrl);
// Start receiving and playing audio
audio.start();
