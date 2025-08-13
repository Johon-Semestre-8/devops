#Sistema de monitoreo - Grupo 3 - Mathias Pena - Sebastian Rivero

from flask import Flask
import psutil
import time

app = Flask(__name__)

# calibrar CPU para que no quede en 0
psutil.cpu_percent(interval=None)

# almacenar valores previos de disco
prev_disk = psutil.disk_io_counters()

@app.route("/")
def index():
    global prev_disk

    # CPU y RAM
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent

    # Disco: calcular bytes leídos/escritos por segundo
    curr_disk = psutil.disk_io_counters()
    read_per_sec = (curr_disk.read_bytes - prev_disk.read_bytes) / 1024  # KB/s
    write_per_sec = (curr_disk.write_bytes - prev_disk.write_bytes) / 1024  # KB/s
    prev_disk = curr_disk

    # HTML simple con auto-refresh cada 2s
    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2">
        <title>Monitoreo del Sistema</title>
    </head>
    <body>
        <h1>Monitoreo del Sistema</h1>
        <p><b>CPU:</b> {cpu}%<br>
           <b>RAM:</b> {ram}%<br>
           <b>Disco:</b> Lectura: {read_per_sec:.1f} KB/s, Escritura: {write_per_sec:.1f} KB/s</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
    
    # Para ver el monitoreo de la PC:
    # En la misma PC: http://localhost:5000
    # En otro dispositivo dentro de la misma red: http://IP_DE_LA_PC:5000