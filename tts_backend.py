"""
Flask Backend for TTS-RVC-API Integration
Handles text-to-speech requests from the frontend and forwards them to TTS-RVC-API
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests
import json
import time
import logging
from io import BytesIO
import config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests from HTML file

@app.route('/generate-speech', methods=['POST'])
def generate_speech():
    """
    Handle text-to-speech generation requests
    
    Expected JSON payload:
    {
        "speaker_name": str,  # e.g., "speaker3"
        "input_text": str,    # Text to convert to speech
        "emotion": str,       # One of: happy, sad, angry, dull, Surprise
        "speed": float        # 1.0 - 2.0
    }
    """
    try:
        # Get request data
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Extract parameters
        speaker_name = data.get('speaker_name', config.DEFAULT_SPEAKER)
        input_text = data.get('input_text', '')
        emotion = data.get('emotion', config.DEFAULT_EMOTION)
        speed = float(data.get('speed', config.DEFAULT_SPEED))
        
        # Validate input
        if not input_text:
            return jsonify({"error": "No text provided"}), 400
        
        if emotion not in config.SUPPORTED_EMOTIONS:
            logger.warning(f"Unsupported emotion '{emotion}', using default")
            emotion = config.DEFAULT_EMOTION
        
        if not (0.5 <= speed <= 2.0):
            logger.warning(f"Speed {speed} out of range, clamping to 1.0-2.0")
            speed = max(0.5, min(2.0, speed))
        
        # Prepare payload for TTS-RVC-API
        payload = {
            "speaker_name": speaker_name,
            "input_text": input_text,
            "emotion": emotion,
            "speed": speed
        }
        
        logger.info(f"Generating speech: speaker={speaker_name}, emotion={emotion}, speed={speed}, text_length={len(input_text)}")
        
        # Make request to TTS-RVC-API
        headers = {'Content-Type': 'application/json'}
        start_time = time.time()
        
        response = requests.post(
            config.TTS_RVC_API_URL,
            headers=headers,
            data=json.dumps(payload),
            timeout=400  # 60 second timeout
        )
        
        end_time = time.time()
        logger.info(f"TTS-RVC-API response time: {end_time - start_time:.2f} seconds")
        
        # Check response
        if response.status_code == 200:
            # Return audio file
            audio_content = response.content
            logger.info(f"Audio generated successfully, size: {len(audio_content)} bytes")
            
            # Create BytesIO object for the audio
            audio_io = BytesIO(audio_content)
            audio_io.seek(0)
            
            return send_file(
                audio_io,
                mimetype='audio/wav',
                as_attachment=True,
                download_name='generated_audio.wav'
            )
        else:
            error_msg = f"TTS-RVC-API error: {response.text}"
            logger.error(error_msg)
            return jsonify({"error": error_msg}), response.status_code
            
    except requests.exceptions.ConnectionError:
        error_msg = "Cannot connect to TTS-RVC-API server. Make sure it's running on localhost:8000"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 503
        
    except requests.exceptions.Timeout:
        error_msg = "TTS-RVC-API request timed out"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 504
        
    except Exception as e:
        error_msg = f"Error generating speech: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return jsonify({"error": error_msg}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    try:
        # Try to ping TTS-RVC-API server
        response = requests.get(config.TTS_RVC_API_URL.replace('/generate', '/'), timeout=5)
        tts_rvc_status = "connected" if response.status_code < 500 else "error"
    except:
        tts_rvc_status = "disconnected"
    
    return jsonify({
        "status": "running",
        "tts_rvc_api": tts_rvc_status,
        "tts_rvc_api_url": config.TTS_RVC_API_URL
    })

if __name__ == '__main__':
    logger.info(f"Starting Flask backend on {config.FLASK_HOST}:{config.FLASK_PORT}")
    logger.info(f"TTS-RVC-API URL: {config.TTS_RVC_API_URL}")
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=config.DEBUG_MODE
    )
