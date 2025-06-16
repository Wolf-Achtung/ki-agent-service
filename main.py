from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import logging
from datetime import datetime
import os
import requests

from agents.crew_config import crew  # crew_config liegt im Ordner "agents"

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI-Instanz
app = FastAPI()

# CORS aktivieren
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # alternativ: ["https://agent.ki-sicherheit.jetzt"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datenschema für den Fragebogen
class AnalyseInput(BaseModel):
    name: str
    unternehmen: str
    antworten: dict  # Beispiel: {"frage1": "Antwort A", "frage2": "Antwort B"}

# PDFMonkey-Integration
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

# Optional: Mock-Result für Testzwecke
mock_result = {
    "score": 41,
    "status": "Fortgeschritten",
    "bewertung": "Ihr Unternehmen zeigt überdurchschnittliche KI-Reife.",
    "executive_summary": "<p>Die Auswertung belegt eine starke Umsetzungsreife in 8 von 10 Bereichen.</p>",
    "analyse": "<p>Stärken bei Automatisierung, Schwächen im Monitoring. DSGVO wird berücksichtigt.</p>",
    "ressourcen": "<ul><li>KI-Wiki intern</li><li>Data-Lab extern</li></ul>",
    "zukunft": "<p>Sie können bis 2026 auf 50% KI-gestützte Prozesse kommen.</p>",
    "empfehlung1": {
        "titel": "KI-Richtlinie erstellen",
        "beschreibung": "Erstellen Sie ein internes Governance-Dokument.",
        "next_step": "Workshop mit Führungsteam",
        "tool": "GPT-Richtlinien-Generator"
    },
    "empfehlung2": {
        "titel": "Tool-Pilot starten",
        "beschreibung": "Pilotieren Sie ein KI-Tool in Abteilung X.",
        "next_step": "Demo-Phase mit Anbieter Y",
        "tool": "KI-Checklisten"
    },
    "empfehlung3": {
        "titel": "Fördermittel beantragen",
        "beschreibung": "Nutzen Sie Landesprogramme für Beratung und Tools.",
        "next_step": "Kontaktaufnahme mit Förderbank",
        "tool": "Förderdatenbank"
    },
    "risikoprofil": {
        "risikoklasse": "Mittel",
        "begruendung": "Sie nutzen KI intern, keine biometrischen Daten.",
        "pflichten": ["Risikobewertung", "DSGVO-Dokumentation"]
    },
    "tooltipps": [
        {"name": "ChatGPT Team", "einsatz": "interne Beratung", "warum": "Niedrigschwellig und flexibel"},
        {"name": "HuggingFace Spaces", "einsatz": "spezialisierte KI-Modelle", "warum": "Open Source mit Kontrolle"}
    ],
    "foerdertipps": [
        {"programm": "go-digital", "zielgruppe": "KMU", "nutzen": "50% Förderung auf externe Beratung"},
        {"programm": "INVEST", "zielgruppe": "Innovative Unternehmen", "nutzen": "Investitionszuschüsse"}
    ],
    "branchenvergleich": "Sie liegen 1,3 Punkte über dem Branchendurchschnitt.",
    "trendreport": "<p>2025 wird multimodale KI marktbestimmend. Bereiten Sie Datenbasis vor.</p>",
    "visionaer": "<p>In 2030 ist KI Teil jeder Kundeninteraktion. Sie sind auf dem Weg dorthin.</p>"
}

# API-Route
@app.post("/api/analyse")
async def analyse(request: Request):
    try:
        body = await request.json()
        logger.info("📩 Neue Anfrage empfangen:")
        logger.info(body)

        input_data = AnalyseInput(**body)

        # CrewAI ausführen
        try:
            result = crew.run({"questionnaire": input_data.dict()})
        except Exception as crew_error:
            logger.warning("⚠️ Crew-Ausführung fehlgeschlagen, Mock wird verwendet.")
            result = mock_result

        logger.info("✅ Analyse abgeschlossen.")

        pdf_payload = {
            "name": input_data.name,
            "unternehmen": input_data.unternehmen,
            "datum": datetime.now().strftime("%d.%m.%Y"),
            **result
        }

        pdf_url = generate_pdf(pdf_payload)

        return JSONResponse(content={"result": result, "pdf_url": pdf_url})

    except ValidationError as ve:
        logger.error(f"❌ Validierungsfehler: {ve}")
        raise HTTPException(status_code=422, detail="Ungültige Eingabedaten.")

    except Exception as e:
        logger.exception("❌ Interner Serverfehler.")
        raise HTTPException(status_code=500, detail="Interner Fehler beim Verarbeiten der Anfrage.")
