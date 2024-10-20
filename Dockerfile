# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the client code
COPY azure_client.py .

# Set environment variables (override in Kubernetes or Docker run commands)
ENV TELEMETRY_URL="http://192.168.3.101:8002/telemetry"
ENV AZURE_REST_API_URL="https://orin-nano-telemetry-apim.azure-api.net/processTelemetry"

# Command to run the client script
CMD ["python3", "azure_client.py"]