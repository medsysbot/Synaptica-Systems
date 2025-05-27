"""Aplicación principal de Synaptica Systems Tester.

Este módulo expone una instancia de :class:`FastAPI` con una ruta de prueba y
monta la carpeta ``public`` para servir archivos estáticos. Está pensado para
ser el punto de partida de funcionalidades más complejas.
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Montar la carpeta ``public`` para que los archivos estáticos estén
# disponibles en ``/public``.
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/saludo")
def saludo() -> dict:
    """Endpoint inicial que devuelve un saludo básico."""
    return {"mensaje": "Hola desde Synaptica Systems Tester"}


@app.get("/")
def serve_tester() -> FileResponse:
    return FileResponse(os.path.join("public", "synaptica-tester.html"), media_type="text/html")
