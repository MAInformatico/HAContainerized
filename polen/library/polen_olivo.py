#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import re

PORT = 8000  # puerto local

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        URL = "https://polen.redugr.es/provincias/granada/"
        nivel = 0
        try:
            r = requests.get(URL, timeout=10)
            html = r.text.lower()
            match = re.search(r'olivo.*?(\d+)', html)
            if match:
                nivel = int(match.group(1))
        except:
            pass

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(nivel).encode())

with HTTPServer(('', PORT), Handler) as server:
    print(f"Servidor REST escuchando en puerto {PORT}")
    server.serve_forever()