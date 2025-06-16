from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import logging
import os
import requests
from datetime import datetime

from agents.crew_config import crew  # crew_config liegt im Ordner "agents"

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI-Instanz
app = FastAPI()

# CORS aktivieren
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://agent.ki-sicherheit.jetzt",
    "http://localhost:5500",  # für lokale Tests
]

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Datenschema für den Fragebogen
class AnalyseInput(BaseModel):
    name: str
    unternehmen: str
    antworten: dict  # Beispiel: {"frage1": "Antwort A", "frage2": "Antwort B"}

# API-Route
@app.options("/api/analyse")
async def options_handler():
    return JSONResponse(status_code=200)

@app.post("/api/analyse")
async def analyse(request: Request):
    try:
        body = await request.json()
        logger.info("🆕 Neue Anfrage empfangen:")
        logger.info(body)

        input_data = AnalyseInput(**body)

        logger.info("✅ Eingabe validiert. Starte Mock-Analyse.")

        result = {
            "score": 85,
            "status": "Vorreiter",
            "bewertung": "Sie gehören zu den führenden Unternehmen im KI-Einsatz.",
            "name": input_data.name,
            "unternehmen": input_data.unternehmen,
            "datum": datetime.now().strftime("%d.%m.%Y")
        }

        logger.info("✅ Analyse abgeschlossen. Generiere PDF...")

        pdf_url = generate_pdf(result)

        return JSONResponse(content={"result": result, "pdf_url": pdf_url})

    except ValidationError as ve:
        logger.error(f"❌ Validierungsfehler: {ve}")
        raise HTTPException(status_code=422, detail="Ungültige Eingabedaten.")

    except Exception as e:
        logger.exception("❌ Interner Serverfehler.")
        raise HTTPException(status_code=500, detail="Interner Fehler beim Verarbeiten der Anfrage.")


def generate_pdf(data: dict) -> str:
    api_key = os.getenv("PDFMONKEY_API_KEY")
    template_id = os.getenv("PDFMONKEY_TEMPLATE_ID")

    payload = {
        "document": {
            "document_template_id": template_id,
            "payload": data
        }
    }

    response = requests.post(
        "https://api.pdfmonkey.io/api/v1/documents",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    if response.status_code != 201:
        raise Exception(f"PDFMonkey-Fehler: {response.text}")

    document = response.json()["data"]
    return document["attributes"]["download_url"]
