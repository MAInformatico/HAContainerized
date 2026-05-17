#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import json
import time

PORT = 8000
URL = "https://polen.redugr.es/provincias/granada/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

CACHE_TIME = 3600  # 1 hora

SCALE = {
    "nulo": 0,
    "bajo": 1,
    "=": 1,
    "medio": 2,
    "↑": 2,
    "alto": 3,
    "↑↑": 3,
    "extremo": 4,
    "↑↑↑": 4,
}

last_values = {
    "olivo": {"symbol": None, "value": None},
    "gramineas": {"symbol": None, "value": None},
}

last_update = 0


# ----------------------------
# FETCH HTML
# ----------------------------
def fetch():
    r = requests.get(URL, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.text


# ----------------------------
# TU LÓGICA (SIN CAMBIOS IMPORTANTES)
# ----------------------------
def normalize_value(v):
    if not v:
        return None, None

    v = v.strip().lower()

    if v in SCALE:
        return v, SCALE[v]

    return v, SCALE.get(v)


def extract_from_blocks(soup):
    result = {}

    blocks = soup.find_all(["tr", "div", "td", "li"])

    for b in blocks:
        text = " ".join(b.get_text(" ", strip=True).lower().split())

        # OLIVO
        if "olivo" in text:
            for k in SCALE.keys():
                if k in text:
                    sym, val = normalize_value(k)
                    result["olivo"] = (sym, val)

        # GRAMÍNEAS
        if "gram" in text:
            for k in SCALE.keys():
                if k in text:
                    sym, val = normalize_value(k)
                    result["gramineas"] = (sym, val)

    return result


# ----------------------------
# CACHE + PARSE
# ----------------------------
def get_data():
    global last_values, last_update

    now = time.time()

    # cache activa
    if now - last_update < CACHE_TIME:
        return last_values

    try:
        html = fetch()
        soup = BeautifulSoup(html, "html.parser")

        data = extract_from_blocks(soup)

        # actualizar solo si hay datos válidos
        if "olivo" in data:
            last_values["olivo"] = {
                "symbol": data["olivo"][0],
                "value": data["olivo"][1],
            }

        if "gramineas" in data:
            last_values["gramineas"] = {
                "symbol": data["gramineas"][0],
                "value": data["gramineas"][1],
            }

        last_update = now

    except Exception as e:
        print("Error scraping:", e)

    return last_values


# ----------------------------
# SERVIDOR HTTP PARA HOME ASSISTANT
# ----------------------------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_data()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())


# ----------------------------
# START SERVER
# ----------------------------
if __name__ == "__main__":
    print(f"Servidor polen activo en http://localhost:{PORT}")
    HTTPServer(("", PORT), Handler).serve_forever()
