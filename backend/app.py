from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
from collections import deque
import os

app = Flask(__name__)

# Store the latest 100 telemetry readings
telemetry_history = deque(maxlen=100)

# Path to dashboard folder
DASHBOARD_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "dashboard")
)


@app.route("/")
def dashboard():
    return send_from_directory(DASHBOARD_FOLDER, "index.html")


@app.route("/api/telemetry", methods=["POST"])
def receive_telemetry():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON data received"
        }), 400

    telemetry = {
        "device_id": data.get("device_id", "unknown"),
        "heart_rate": data.get("heart_rate"),
        "spo2": data.get("spo2"),
        "timestamp": data.get(
            "timestamp",
            datetime.now().isoformat()
        )
    }

    telemetry_history.append(telemetry)

    print("Received telemetry:")
    print(telemetry)

    return jsonify({
        "status": "success",
        "message": "Telemetry received"
    })


@app.route("/api/latest", methods=["GET"])
def latest():

    if not telemetry_history:
        return jsonify({
            "status": "no_data"
        })

    return jsonify(telemetry_history[-1])


@app.route("/api/history", methods=["GET"])
def history():

    return jsonify(list(telemetry_history))


if __name__ == "__main__":

    print("===================================")
    print(" HEALTHCARE TELEMETRY BACKEND")
    print("===================================")
    print("Dashboard: http://127.0.0.1:5000")
    print("API:       http://127.0.0.1:5000/api/telemetry")
    print()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )