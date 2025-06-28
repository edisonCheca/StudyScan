# backend/app/main.py

from fastapi import FastAPI

# Crea una instancia de la aplicación FastAPI
app = FastAPI(
    title="StudyScan API",
    description="API para procesar documentos con OCR e IA y generar material de estudio.",
    version="0.1.0",
)

# Define un endpoint de prueba en la raíz ("/")
# El decorador @app.get("/") le dice a FastAPI que esta función
# maneja las peticiones GET a la URL raíz.
@app.get("/", tags=["Health Check"])
def read_root():
    """
    Endpoint raíz para verificar que la API está funcionando.
    """
    return {"status": "ok", "message": "Welcome to StudyScan API!"}

# Define un endpoint de "ping" para una verificación simple
@app.get("/ping", tags=["Health Check"])
def ping():
    """
    Endpoint simple para verificar la disponibilidad de la API.
    Responde con 'pong'.
    """
    return {"ping": "pong"}