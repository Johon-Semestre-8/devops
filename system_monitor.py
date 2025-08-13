from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return jsonify({
        "CPU (%)": cpu_percent,
        "RAM (%)": ram.percent,
        "RAM_Usada_MB": ram.used // (1024 * 1024),
        "RAM_Total_MB": ram.total // (1024 * 1024),
        "Disco (%)": disk.percent,
        "Disco_Usado_GB": disk.used // (1024**3),
        "Disco_Total_GB": disk.total // (1024**3)
    })

if __name__ == "__main__":
    # Escucha en todas las interfaces para que sea accesible desde la LAN
    app.run(host="0.0.0.0", port=5000)
