import psutil
import requests
import time
import json
SERVER_URL = 'http://192.168.208.1:5000/metrics'  
def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return {
        'cpu': cpu,
        'ram': ram,
        'disk': disk
    }
while True:
    metrics = get_metrics()
    try:
        response = requests.post(SERVER_URL, json=metrics)
        print(f"Sent metrics: {metrics} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error sending metrics: {e}")
    time.sleep(10)  