import time
from ping3 import ping
import requests
from requests.auth import HTTPBasicAuth

HOST = "192.168.0.1"
URL = "http://192.168.0.1"
INTERVALO = 5
USUARIO = "admin"
CONTRASENA = "admin"

print(f"Monitoreando red y web contra {HOST} / {URL} (CTRL+C para detener)\n")

while True:
    try:
        latencia = ping(HOST, timeout=2)
        if latencia is None:
            ping_msg = f"{time.strftime('%H:%M:%S')} - Ping: Sin respuesta"
        else:
            ping_msg = f"{time.strftime('%H:%M:%S')} - Ping: {latencia*1000:.2f} ms"
        
        try:
            inicio = time.time()
            respuesta = requests.get(
                URL,
                timeout=3,
                auth=HTTPBasicAuth(USUARIO, CONTRASENA)
            )
            tiempo_respuesta = (time.time() - inicio) * 1000

            if respuesta.status_code == 200:
                web_msg = f"Web: Disponible - Tiempo de respuesta: {tiempo_respuesta:.2f} ms"
            else:
                web_msg = f"Web: Caída - Código HTTP: {respuesta.status_code}"
        except requests.exceptions.Timeout:
            web_msg = "Web: Sin respuesta (timeout)"
        except requests.exceptions.RequestException as e:
            web_msg = f"Web: Error: {e}"
        
        print(f"{ping_msg} | {web_msg}")
        
        time.sleep(INTERVALO)

    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
        break
    except Exception as e:
        print(f"Error general: {e}")
        time.sleep(INTERVALO)
