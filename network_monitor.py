import subprocess
import time
import speedtest
import platform
from flask import Flask, render_template, jsonify
import threading
import datetime

app = Flask(__name__)

# Datos de monitoreo (compartidos entre hilos)
monitoring_data = {
    'ping': [],
    'download': [],
    'upload': [],
    'uptime': [],
    'last_update': None
}

# Configuración
MONITORING_INTERVAL = 60  # segundos
HOST_TO_PING = "google.com"  # host para medir latencia

def get_ping():
    """Obtiene el ping (latencia) a un host determinado"""
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '4', HOST_TO_PING]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            output = result.stdout
            if 'time=' in output:
                time_values = [float(line.split('time=')[1].split(' ms')[0]) 
                             for line in output.split('\n') if 'time=' in line]
                avg_ping = sum(time_values) / len(time_values)
                return round(avg_ping, 2)
        return None
    except:
        return None

def get_speed():
    """Mide el ancho de banda (throughput) usando speedtest"""
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        return {
            'download': round(st.results.download / 1_000_000, 2),  # en Mbps
            'upload': round(st.results.upload / 1_000_000, 2)       # en Mbps
        }
    except:
        return {'download': None, 'upload': None}

def monitor_network():
    """Función que realiza el monitoreo periódico"""
    while True:
        # Obtener métricas
        ping = get_ping()
        speed = get_speed()
        
        # Almacenar datos (mantener solo las últimas 24 horas)
        timestamp = datetime.datetime.now()
        
        if ping is not None:
            monitoring_data['ping'].append({
                'time': timestamp,
                'value': ping
            })
            # Mantener solo los últimos 1440 registros (24 horas si se mide cada minuto)
            monitoring_data['ping'] = monitoring_data['ping'][-1440:]
        
        if speed['download'] is not None:
            monitoring_data['download'].append({
                'time': timestamp,
                'value': speed['download']
            })
            monitoring_data['download'] = monitoring_data['download'][-1440:]
        
        if speed['upload'] is not None:
            monitoring_data['upload'].append({
                'time': timestamp,
                'value': speed['upload']
            })
            monitoring_data['upload'] = monitoring_data['upload'][-1440:]
        
        # Calcular uptime (disponibilidad)
        uptime_percent = 100
        if len(monitoring_data['ping']) > 0:
            successful_pings = sum(1 for item in monitoring_data['ping'] if item['value'] is not None)
            uptime_percent = (successful_pings / len(monitoring_data['ping'])) * 100
        
        monitoring_data['uptime'].append({
            'time': timestamp,
            'value': round(uptime_percent, 2)
        })
        monitoring_data['uptime'] = monitoring_data['uptime'][-1440:]
        
        monitoring_data['last_update'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
        # Esperar hasta la próxima medición
        time.sleep(MONITORING_INTERVAL)

@app.route('/')
def dashboard():
    """Página principal del dashboard"""
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    """Endpoint para obtener datos en formato JSON"""
    # Preparar datos para el gráfico (solo los últimos 60 puntos para mejor rendimiento)
    chart_data = {
        'ping': monitoring_data['ping'][-60:],
        'download': monitoring_data['download'][-60:],
        'upload': monitoring_data['upload'][-60:],
        'uptime': monitoring_data['uptime'][-60:],
        'last_update': monitoring_data['last_update'],
        'current_status': {
            'ping': monitoring_data['ping'][-1]['value'] if len(monitoring_data['ping']) > 0 else None,
            'download': monitoring_data['download'][-1]['value'] if len(monitoring_data['download']) > 0 else None,
            'upload': monitoring_data['upload'][-1]['value'] if len(monitoring_data['upload']) > 0 else None,
            'uptime': monitoring_data['uptime'][-1]['value'] if len(monitoring_data['uptime']) > 0 else None
        }
    }
    return jsonify(chart_data)

if __name__ == '__main__':
    # Iniciar el monitoreo en segundo plano
    monitor_thread = threading.Thread(target=monitor_network)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    # Iniciar el servidor web
    app.run(host='0.0.0.0', port=5000, debug=False)