import requests
import json
import time
import os

# Set environment variables for these in Docker or Kubernetes
TELEMETRY_URL = os.getenv("TELEMETRY_URL", "http://<orin-ip>:8002/telemetry")
AZURE_REST_API_URL = os.getenv("AZURE_REST_API_URL", "https://<your-function-app-name>.azurewebsites.net/api/processTelemetry")

def fetch_telemetry():
    try:
        response = requests.get(TELEMETRY_URL)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching telemetry: {e}")
        return None

def push_to_azure(data):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(AZURE_REST_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            print("Data successfully sent to Azure.")
        else:
            print(f"Failed to send data to Azure: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to Azure: {e}")

if __name__ == "__main__":
    while True:
        telemetry_data = fetch_telemetry()
        if telemetry_data:
            push_to_azure(telemetry_data)
        time.sleep(10)  # Fetch and send telemetry every 10 seconds (adjust as needed)