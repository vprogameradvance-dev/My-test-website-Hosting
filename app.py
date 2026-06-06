from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# 1. This handles the main homepage
@app.route('/')
def home():
    return "<h1>Welcome to my School Project Backend!</h1><p>The server is running successfully.</p>"

# 2. This is a sample API endpoint that returns data
@app.route('/api/data', methods=['GET'])
def get_data():
    project_info = {
        "status": "success",
        "project_name": "School Project",
        "version": "1.0"
    }
    return jsonify(project_info)

# 3. This tells the server how to run on Render
if __name__ == '__main__':
    # Render assigns a temporary port, so we must read it from the environment
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
