import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="processTelemetry")
@app.route(route="processTelemetry", auth_level=func.AuthLevel.ANONYMOUS)
def process_telemetry(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received a request to process telemetry.')

    try:
        telemetry_data = req.get_json()
        logging.info(f"Telemetry data received: {telemetry_data}")
        # Add logic here to process or store telemetry_data
        return func.HttpResponse("Telemetry data processed successfully.", status_code=200)
    except ValueError:
        return func.HttpResponse("Invalid JSON received.", status_code=400)