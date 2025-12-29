from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS (required for browser → backend calls)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Backend is running 🚀"
    })

@app.route("/", methods=["GET"])
def root():
    return "Backend root is working", 200

if __name__ == "__main__":
    # Important: host=0.0.0.0 so Kubernetes can access it
    app.run(host="0.0.0.0", port=5000)
