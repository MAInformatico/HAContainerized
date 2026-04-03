#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import re
import time

PORT = 8000

URL = "https://polen.redugr.es/provincias/granada/"
CACHE_TIME = 3600  # 1 hora

last_value = 0
last_update = 0

def get_polen():
    global last_value, last_update

    now = time.time()

    # Si no ha pasado el tiempo, devuelve cache
    if now - last_update < CACHE_TIME:
        return last_value

    try:
        r = requests.get(URL, timeout=10)
        html = r.text.lower()
        match = re.search(r'olivo.*?(\d+)', html)
        if match:
            last_value = int(match.group(1))
            last_update = now
    except:
        pass

    return last_value


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        nivel = get_polen()

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(nivel).encode())


with HTTPServer(('', PORT), Handler) as server:
    print(f"Servidor REST con cache en puerto {PORT}")
    server.serve_forever()
    print("Valor polen:", last_value)
