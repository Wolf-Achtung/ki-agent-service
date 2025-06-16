from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import logging

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

# API-Route
@app.post("/api/analyse")
async def analyse(request: Request):
    try:
        body = await request.json()
        logger.info("📩 Neue Anfrage empfangen:")
        logger.info(body)

        input_data = AnalyseInput(**body)

        # CrewAI ausführen
        result = crew.run({"questionnaire": input_data.dict()})
        logger.info("✅ Analyse abgeschlossen.")
        return JSONResponse(content={"result": result})

    except ValidationError as ve:
        logger.error(f"❌ Validierungsfehler: {ve}")
        raise HTTPException(status_code=422, detail="Ungültige Eingabedaten.")

    except Exception as e:
        logger.exception("❌ Interner Serverfehler.")
        raise HTTPException(status_code=500, detail="Interner Fehler beim Verarbeiten der Anfrage.")
