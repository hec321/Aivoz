# TTS-RVC-API Server Setup Guide

## Prerequisites
- Python 3.8 or higher
- Git

## Step 1: Clone TTS-RVC-API Repository

Open a terminal and run:

```bash
git clone https://github.com/skshadan/TTS-RVC-API.git
cd TTS-RVC-API
```

## Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment:
- **Windows**: `.venv\Scripts\activate`
- **Linux/Mac**: `source .venv/bin/activate`

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
pip install TTS
```

## Step 4: Configure Speaker Models

The TTS-RVC-API requires RVC v2 models. You need to:

1. Create a `models` directory structure:
```
TTS-RVC-API/
└── models/
    └── speaker1/
        ├── speaker1.pth
        └── speaker1.index
```

2. Place your RVC model files (.pth and .index) in the speaker directories

3. Update `config.toml` with the path to your models:
```toml
model_dir = "./models/speaker1"
```

> **Note**: If you don't have RVC models yet, you can:
> - Train your own using RVC (requires 2-3 minutes of audio)
> - Download pre-trained models from the RVC community
> - Use default TTS voices without RVC (modify the API accordingly)

## Step 5: Run the Server

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The server should start at `http://localhost:8000`

## Step 6: Test the Server

Open another terminal and test:

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"speaker_name": "speaker1", "input_text": "Hello world", "emotion": "Dull", "speed": 1.0}' \
  --output test_audio.wav
```

If successful, you should have a `test_audio.wav` file.

## Troubleshooting

### Issue: "No module named 'TTS'"
**Solution**: Install TTS library: `pip install TTS`

### Issue: "ModuleNotFoundError: No module named 'app'"
**Solution**: Make sure you're in the TTS-RVC-API directory when running uvicorn

### Issue: "Model not found"
**Solution**: 
1. Check that your model files exist in the correct directory
2. Verify the `config.toml` file has the correct model path
3. Ensure the speaker_name in requests matches your model directory name

### Issue: Server won't start on port 8000
**Solution**: Port may be in use. Try a different port:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001
```
Then update `config.py` in the AIvoz backend to match.

## Next Steps

Once the TTS-RVC-API server is running:
1. Keep the server running in one terminal
2. In another terminal, navigate to your AIvoz audio directory
3. Follow the instructions in `README_BACKEND.md` to start the Flask backend
