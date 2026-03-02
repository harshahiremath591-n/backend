from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your Netlify site to access this API

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/api/data')
def get_data():
    # This is an example API endpoint [cite: 13]
    return jsonify({"status": "success", "data": "Hello from Python!"})

if __name__ == '__main__':
    # Render uses dynamic ports; this helps it run locally or on the cloud
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
