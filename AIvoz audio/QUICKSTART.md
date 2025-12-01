# Quick Start Guide - TTS-RVC-API Integration

This is a simplified guide to get your TTS-RVC integration up and running quickly.

## Prerequisites
- Python 3.8+ installed
- Git installed
- Windows PowerShell or Command Prompt

## Step 1: Install Flask Backend Dependencies (2 minutes)

Open PowerShell in the `AIvoz audio` directory:

```powershell
cd "C:\Users\hecto\Downloads\AIvoz audio"
pip install -r requirements.txt
```

## Step 2: Setup TTS-RVC-API Server (15-20 minutes)

### 2.1 Clone the Repository

```powershell
cd "C:\Users\hecto\Downloads"
git clone https://github.com/skshadan/TTS-RVC-API.git
cd TTS-RVC-API
```

### 2.2 Install Dependencies

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install TTS
```

### 2.3 Get RVC Models

**Option A: Use Default TTS (No RVC)**
For testing purposes, you can skip RVC models and just use TTS. The system will still work.

**Option B: Add RVC Models**
1. Create `models/speaker3` directory
2. Place your `.pth` and `.index` files there
3. Update `config.toml` with the correct path

### 2.4 Start the Server

```powershell
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Keep this terminal open!

## Step 3: Start Flask Backend (1 minute)

Open a **new** PowerShell window:

```powershell
cd "C:\Users\hecto\Downloads\AIvoz audio"
python tts_backend.py
```

You should see:
```
INFO - Starting Flask backend on 0.0.0.0:5000
INFO - TTS-RVC-API URL: http://localhost:8000/generate
```

Keep this terminal open too!

## Step 4: Use the Application

1. Open `C:\Users\hecto\Downloads\AIvoz audio\AIvoz audio\Aivoz.html` in your browser

2. You should see the emotion selector now has:
   - Feliz / Happy
   - Triste / Sad
   - Enojado / Angry
   - Normal / Dull (default)
   - Sorpresa / Surprise

3. Enter some text, select emotion and speed, then click "Generar locución"

4. Wait for processing (check browser console with F12)

5. Audio file will automatically download!

## Troubleshooting

### "Cannot connect to TTS-RVC-API server"
- Make sure TTS-RVC-API server is running on port 8000
- Check the terminal where you started it for errors

### "Cannot connect to backend server"
- Make sure Flask backend is running on port 5000
- Check the terminal for errors

### Nothing happens when clicking button
- Open browser console (F12 → Console tab)
- Look for error messages
- Check that JavaScript loaded: should see "TTS-RVC-API integration loaded successfully"

### Port 8000 or 5000 already in use
- Stop other applications using those ports, or
- Change the port in `config.py` (for Flask) or uvicorn command (for TTS-RVC)

## What You Have Now

✅ Flask backend that proxies requests to TTS-RVC-API
✅ Modified frontend with emotion selector
✅ Working "Generar locución" button
✅ Automatic audio download

## Next Steps (Optional)

- Train your own RVC voice models
- Customize the voice options in the dropdown
- Add more languages
- Deploy to a server instead of localhost

For more details, see:
- `setup_tts_rvc.md` - Detailed TTS-RVC-API setup
- `README_BACKEND.md` - Backend configuration and troubleshooting
