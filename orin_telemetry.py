from fastapi import FastAPI
import psutil
import netifaces
import json

app = FastAPI()

@app.get("/telemetry")
def get_telemetry():
    telemetry_data = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory()._asdict(),
        "network": get_network_info()
    }
    return telemetry_data

def get_network_info():
    interfaces = netifaces.interfaces()
    network_info = {}
    
    for interface in interfaces:
        ifaddresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in ifaddresses:
            ipv4_info = ifaddresses[netifaces.AF_INET][0]
            network_info[interface] = {
                "ip_address": ipv4_info.get('addr', 'N/A'),
                "netmask": ipv4_info.get('netmask', 'N/A')
            }
    
    return network_info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)