import random
import time
import requests
from datetime import datetime


BACKEND_URL = "http://127.0.0.1:5000/api/telemetry"


def generate_heart_rate():
    return random.randint(65, 90)


def generate_spo2():
    return random.randint(96, 100)


def generate_telemetry():

    return {
        "device_id": "ESP32-CAM-001",
        "heart_rate": generate_heart_rate(),
        "spo2": generate_spo2(),
        "timestamp": datetime.now().isoformat()
    }


def send_to_backend(data):

    try:

        response = requests.post(
            BACKEND_URL,
            json=data,
            timeout=5
        )

        if response.status_code == 200:

            print("✓ Sent to backend")

        else:

            print(
                "✗ Backend error:",
                response.status_code,
                response.text
            )

    except requests.exceptions.RequestException as error:

        print("✗ Could not connect to backend:", error)


def main():

    print("===================================")
    print(" MAX30102 SENSOR SIMULATOR")
    print("===================================")
    print("Device: ESP32-CAM-001")
    print("Mode:   SIMULATION")
    print("Backend:", BACKEND_URL)
    print()

    while True:

        telemetry = generate_telemetry()

        print("Heart Rate :", telemetry["heart_rate"], "BPM")
        print("SpO2       :", telemetry["spo2"], "%")
        print("Timestamp  :", telemetry["timestamp"])

        send_to_backend(telemetry)

        print("-----------------------------------")

        time.sleep(2)


if __name__ == "__main__":
    main()