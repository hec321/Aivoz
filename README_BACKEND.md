# AIvoz TTS Backend Setup

This guide covers setting up the Flask backend that connects your AIvoz frontend to the TTS-RVC-API server.

## Prerequisites
- Python 3.8+
- TTS-RVC-API server running (see `setup_tts_rvc.md`)

## Installation

### 1. Install Python Dependencies

Open a terminal in the `AIvoz audio` directory and run:

```bash
pip install -r requirements.txt
```

### 2. Configure Settings (Optional)

Edit `config.py` if you need to change:
- TTS-RVC-API server URL (default: `http://localhost:8000/generate`)
- Flask server port (default: 5000)
- Default emotion or speed values

## Running the Backend

### Start the Flask Server

```bash
python tts_backend.py
```

You should see output like:
```
INFO - Starting Flask backend on 0.0.0.0:5000
INFO - TTS-RVC-API URL: http://localhost:8000/generate
 * Running on http://127.0.0.1:5000
```

### Health Check

Open a browser and visit: `http://localhost:5000/health`

You should see:
```json
{
  "status": "running",
  "tts_rvc_api": "connected",
  "tts_rvc_api_url": "http://localhost:8000/generate"
}
```

## Using the Application

1. Make sure both servers are running:
   - TTS-RVC-API server on port 8000
   - Flask backend on port 5000

2. Open `AIvoz audio/Aivoz.html` in your browser

3. Enter text in the textarea

4. Select:
   - Voice/Language
   - Emotion (Happy, Sad, Angry, Dull, Surprise)
   - Speed (0.5x to 2.0x)

5. Click "Generar locución"

6. Wait for the audio to generate (check browser console for progress)

7. The audio file will automatically download as `generated_audio.wav`

## Troubleshooting

### Backend won't start

**Error: "Address already in use"**
- Another application is using port 5000
- Solution: Change `FLASK_PORT` in `config.py` to a different port (e.g., 5001)

**Error: "No module named 'flask'"**
- Dependencies not installed
- Solution: Run `pip install -r requirements.txt`

### Cannot generate audio

**Error: "Cannot connect to TTS-RVC-API server"**
- TTS-RVC-API server is not running
- Solution: Start the TTS-RVC-API server (see `setup_tts_rvc.md`)

**Error: "CORS policy"**
- Browser blocking cross-origin requests
- Solution: Make sure Flask-CORS is installed and the backend is running

### Audio not downloading

- Check browser console for errors (F12 → Console tab)
- Verify the backend logs show successful generation
- Try a different browser
- Check if popup blockers are preventing the download

## Development

### View Logs

The Flask backend logs all requests and errors. Watch the terminal where you ran `python tts_backend.py`.

### Test API Directly

You can test the backend API using curl:

```bash
curl -X POST http://localhost:5000/generate-speech \
  -H "Content-Type: application/json" \
  -d '{"speaker_name": "speaker3", "input_text": "Hello world", "emotion": "happy", "speed": 1.0}' \
  --output test.wav
```

## Architecture

```
Browser (Aivoz.html)
    ↓ POST /generate-speech
Flask Backend (tts_backend.py)
    ↓ POST /generate
TTS-RVC-API Server
    ↓ Returns audio
Flask Backend
    ↓ Returns audio
Browser downloads file
```
