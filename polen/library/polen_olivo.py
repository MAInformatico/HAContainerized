#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import re
import time
import json

PORT = 8000

URL = "https://polen.redugr.es/provincias/granada/"
CACHE_TIME = 3600  # 1 hora

last_values = {"olivo": 0, "gramineas": 0}
last_update = 0

def get_polen():
    global last_values, last_update

    now = time.time()

    # Si no ha pasado el tiempo, devuelve cache
    if now - last_update < CACHE_TIME:
        return last_values

    try:
        r = requests.get(URL, timeout=10)
        html = r.text.lower()

        # Buscar el valor del polen de olivo
        olivo_match = re.search(r'olivo.*?(\d+)', html)
        if olivo_match:
            last_values["olivo"] = int(olivo_match.group(1))

        # Buscar el valor del polen de gramíneas
        gramineas_match = re.search(r'gramíneas.*?(\d+)', html)
        if gramineas_match:
            last_values["gramineas"] = int(gramineas_match.group(1))

        last_update = now
    except:
        pass

    return last_values

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        niveles = get_polen()

        self.send_response(200)
        self.send_header('Content-type','application/json')  # Usamos JSON para los datos
        self.end_headers()
        
        # Devolvemos los niveles de polen en formato JSON
        self.wfile.write(json.dumps(niveles).encode())

with HTTPServer(('', PORT), Handler) as server:
    print(f"Servidor REST con cache en puerto {PORT}")
    server.serve_forever()
    print("Valores de polen:", last_values)
