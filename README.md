
# **RealtimeAgent over WebSockets**

This project demonstrates how to create a voice assistant using Python, FastAPI, WebSockets, and an AG2 RealtimeAgent. The application streams audio from a browser to a FastAPI server and enables real-time voice communication with the RealtimeAgent.

## **Key Features**
- **WebSocket Audio Streaming**: Direct real-time audio streaming between the browser and server.
- **FastAPI Integration**: A lightweight Python backend for handling WebSocket traffic.

## **Prerequisites**

Before you begin, ensure you have the following:
- **Python 3.9+**: The project was tested with `3.9`. Download [here](https://www.python.org/downloads/).
- **API Access**: Access to the OpenAI API (credentials required).

## **Local Setup**

Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/sternakt/RealtimeAgent-WebSocketAudioAdapter.git
cd RealtimeAgent-WebSocketAudioAdapter
```

### **2. Set Up Environment Variables**
Create a `.env` file based on the provided `.env.example`:
```bash
cp .env.example .env
```
Add your OPENAI API credentials to the `.env` file.

### **3. Install Dependencies**
Install the required Python packages using `pip`:
```bash
pip install .
```

### **4. Start the Server**
Run the application with Uvicorn:
```bash
uvicorn realtime_over_websockets.main:app --port 5050
```

## **Test the App**
With the server running, open the client application in your browser. Speak into your microphone, and the AI assistant will respond in real time.

## **License**
This project is licensed under the [MIT License](LICENSE).
