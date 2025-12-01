# Configuration for TTS-RVC-API Integration

# TTS-RVC-API Server Configuration
TTS_RVC_API_URL = "http://localhost:8000/generate"

# Flask Server Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
DEBUG_MODE = True

# Default TTS Parameters
DEFAULT_EMOTION = "Dull"
DEFAULT_SPEED = 1.0
DEFAULT_SPEAKER = "speaker3"

# Supported emotions from TTS-RVC-API
SUPPORTED_EMOTIONS = ["happy", "sad", "angry", "dull", "Surprise"]
