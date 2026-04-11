#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import time
import json

PORT = 8001

# Coordenadas de Granada
LAT = 37.1773
LON = -3.5986

URL = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={LAT}&longitude={LON}&current=pm10"

CACHE_TIME = 1800  # 30 minutos

last_values = {
    "pm10": 0,
    "calima": "desconocida",
    "tendencia": "estable",
    "timestamp": 0
}
last_update = 0


def clasificar_calima(pm10):
    if pm10 < 20:
        return "sin calima"
    elif pm10 < 50:
        return "leve"
    elif pm10 < 100:
        return "moderada"
    else:
        return "intensa"


def calcular_tendencia(actual, anterior):
    delta = actual - anterior

    if abs(delta) < 5:
        return "estable"
    elif delta > 0:
        return "subiendo"
    else:
        return "bajando"


def get_calima():
    global last_values, last_update

    now = time.time()

    if now - last_update < CACHE_TIME:
        return last_values

    try:
        r = requests.get(URL, timeout=10)
        data = r.json()

        pm10_nuevo = data["current"]["pm10"]
        pm10_anterior = last_values["pm10"]

        tendencia = calcular_tendencia(pm10_nuevo, pm10_anterior)

        last_values["pm10"] = pm10_nuevo
        last_values["calima"] = clasificar_calima(pm10_nuevo)
        last_values["tendencia"] = tendencia
        last_values["timestamp"] = int(now)

        last_update = now
    except:
        pass

    return last_values


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        niveles = get_calima()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(niveles).encode())


with HTTPServer(('', PORT), Handler) as server:
    print(f"Servidor REST de calima en puerto {PORT}")
    server.serve_forever()
