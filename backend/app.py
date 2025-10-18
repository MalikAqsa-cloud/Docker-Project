from flask import Flask, request, jsonify
import os
import time
from datetime import datetime

# Create Flask application instance
app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring and load balancers
    Returns service status and timestamp
    """
    return jsonify({
        "status": "healthy",
        "service": "docker-assignment-backend",
        "timestamp": datetime.utcnow().isoformat(),
        "uptime": time.time(),
        "version": "1.0.0"
    }), 200

@app.route('/api/greet', methods=['GET', 'POST'])
def greet():
    """
    Greeting endpoint that accepts name parameter
    Supports both GET and POST methods
    """
    if request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name', 'World')
    else:
        name = request.args.get('name', 'World')
    
    return jsonify({
        "message": f"Hello, {name}! Welcome to Docker Assignment",
        "timestamp": datetime.utcnow().isoformat(),
        "method": request.method
    }), 200

@app.route('/api/echo', methods=['POST'])
def echo():
    """
    Echo endpoint that returns the received data
    Demonstrates request/response handling
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error": "No JSON data provided",
                "message": "Please send JSON data in the request body"
            }), 400
        
        return jsonify({
            "echo": data,
            "timestamp": datetime.utcnow().isoformat(),
            "received_at": time.time()
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": "Invalid JSON data",
            "message": str(e)
        }), 400

if __name__ == '__main__':
    # This will only run if the file is executed directly
    # In production, Gunicorn will handle the WSGI application
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)