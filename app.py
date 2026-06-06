from flask import Flask, jsonify
from flask_cors import CORS # Import the CORS library
import os

app = Flask(__name__)
CORS(app) # This single line tells your backend to accept requests from anywhere!

@app.route('/api/data', methods=['GET'])
def get_data():
    project_info = {
        "message": "Hello from Render! The connection worked!",
        "status": "success"
    }
    return jsonify(project_info)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
