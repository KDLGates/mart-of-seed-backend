"""
Minimalist Flask application for SeedMart backend
This version has all complex functionality removed to ensure it builds without errors
"""
from flask import Flask, jsonify

# Create a minimal Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "Under Construction",
        "message": "SeedMart API is currently being rebuilt. Please check back later."
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "OK",
        "message": "Minimal service running"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "LIMITED",
        "message": "Minimal API service running",
        "database": "Disconnected - Service in maintenance mode"
    })

# This keeps the application simple with no database or external dependencies
if __name__ == '__main__':
    print("Starting minimal SeedMart API in maintenance mode")
    app.run(host='0.0.0.0', port=5000, debug=False)