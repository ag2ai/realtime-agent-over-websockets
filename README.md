
# **RealtimeAgent over WebSockets**

This project demonstrates how to create a voice assistant using Python, FastAPI, WebSockets, and an AG2 RealtimeAgent. The application streams audio from a browser to a FastAPI server and enables real-time voice communication with the RealtimeAgent.

## **Key Features**
- **WebSocket Audio Streaming**: Direct real-time audio streaming between the browser and server.
- **FastAPI Integration**: A lightweight Python backend for handling WebSocket traffic.

## **Prerequisites**

Before you begin, ensure you have the following:
- **Python 3.9+**: The project was tested with `3.9`. Download [here](https://www.python.org/downloads/).
- **An OpenAI account and an OpenAI API Key.** You can sign up [here](https://platform.openai.com/).
  - **OpenAI Realtime API access.**

## **Local Setup**

Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/ag2ai/realtime-agent-over-websockets.git
cd realtime-agent-over-websockets
```

### **2. Set Up Environment Variables**
Create a `OAI_CONFIG_LIST` file based on the provided `OAI_CONFIG_LIST_sample`:
```bash
cp OAI_CONFIG_LIST_sample OAI_CONFIG_LIST
```

#### To use OpenAI Realtime API
1. In the OAI_CONFIG_LIST file, update the `api_key` to your OpenAI API key for the configuration with the tag "gpt-4o-mini-realtime"

#### To use Gemini Live API
1. In the OAI_CONFIG_LIST file, update the `api_key` to your Gemini API key for the configuration with the tag "gemini-realtime"
2. In realtime_over_websockets/main.py update [filter_dict tag](https://github.com/ag2ai/realtime-agent-over-websockets/blob/main/realtime_over_websockets/main.py#L17) to "gemini-realtime"

### (Optional) Create and use a virtual environment

To reduce cluttering your global Python environment on your machine, you can create a virtual environment. On your command line, enter:

```
python3 -m venv env
source env/bin/activate
```

### **3. Install Dependencies**
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### **4. Start the Server**
Run the application with Uvicorn:
```bash
uvicorn realtime_over_websockets.main:app --port 5050
```

## **Test the App**
With the server running, open the client application in your browser by navigating to [http://localhost:5050/start-chat/](http://localhost:5050/start-chat/). Speak into your microphone, and the AI assistant will respond in real time.

## **License**
This project is licensed under the [MIT License](LICENSE).
