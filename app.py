from flask import Flask, jsonify, request
import requests
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Cimeika API!"

@app.route('/data/weather')
def get_weather():
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        logger.error("OPENWEATHERMAP_API_KEY is not set")
        return jsonify({"error": "OPENWEATHERMAP_API_KEY is not set"}), 500
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Weather data fetched successfully: {data}")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        return jsonify({"error": "Failed to fetch weather data"}), 500

@app.route('/data/time')
def get_time():
    from datetime import datetime
    try:
        now = datetime.utcnow()
        logger.info(f"Current time fetched successfully: {now}")
        return jsonify({"time": now.isoformat()})
    except Exception as e:
        logger.error(f"Error fetching current time: {e}")
        return jsonify({"error": "Failed to fetch current time"}), 500

@app.route('/data/astrology')
def get_astrology():
    api_key = os.getenv("FREEASTROLOGYAPI_API_KEY")
    if not api_key:
        logger.error("FREEASTROLOGYAPI_API_KEY is not set")
        return jsonify({"error": "FREEASTROLOGYAPI_API_KEY is not set"}), 500
    sign = "aries"
    url = f"https://api.freeastrologyapi.com/forecast?sign={sign}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Astrology data fetched successfully: {data}")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching astrology data: {e}")
        return jsonify({"error": "Failed to fetch astrology data"}), 500

@app.route('/data/health')
def get_health():
    api_key = os.getenv("HEALTH_API_KEY")
    if not api_key:
        logger.error("HEALTH_API_KEY is not set")
        return jsonify({"error": "HEALTH_API_KEY is not set"}), 500
    url = f"https://api.healthdataapi.com/health?apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Health data fetched successfully: {data}")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching health data: {e}")
        return jsonify({"error": "Failed to fetch health data"}), 500

@app.route('/podia/events', methods=['POST'])
def create_event():
    api_key = os.getenv("GOOGLE_CALENDAR_API_KEY")
    if not api_key:
        logger.error("GOOGLE_CALENDAR_API_KEY is not set")
        return jsonify({"error": "GOOGLE_CALENDAR_API_KEY is not set"}), 500
    event_data = request.json
    url = f"https://www.googleapis.com/calendar/v3/calendars/primary/events?key={api_key}"
    try:
        response = requests.post(url, json=event_data)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Event created successfully: {data}")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating event: {e}")
        return jsonify({"error": "Failed to create event"}), 500

@app.route('/nastiy/mood', methods=['POST'])
def track_mood():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY is not set")
        return jsonify({"error": "OPENAI_API_KEY is not set"}), 500
    mood_data = request.json
    url = f"https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=mood_data, headers=headers)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Mood tracked successfully: {data}")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error tracking mood: {e}")
        return jsonify({"error": "Failed to track mood"}), 500

@app.route('/mala/creative', methods=['POST'])
def upload_creative_work():
    api_key = os.getenv("DROPBOX_API_KEY")
    if not api_key:
        logger.error("DROPBOX_API_KEY is not set")
        return jsonify({"error": "DROPBOX_API_KEY is not set"}), 500
    creative_data = request.json
    url = "https://content.dropboxapi.com/2/files/upload"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Dropbox-API-Arg": "{\"path\": \"/creative_works/file.jpg\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}",
        "Content-Type": "application/octet-stream"
    }
    try:
        response = requests.post(url, data=creative_data, headers=headers)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Creative work uploaded successfully: {data}")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error uploading creative work: {e}")
        return jsonify({"error": "Failed to upload creative work"}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
