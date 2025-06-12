# KI-Briefing Agent Service

## Setup

1. `.env` mit `OPENAI_API_KEY` anlegen.
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload` starten.

## API

POST `/briefing` mit JSON payload:

```json
{
  "branche": "Handel",
  "selbststaendig": "Nein",
  "massnahmen": "...",
  "score": 14,
  "status": "Basis",
  "bewertung": "...",
  "herausforderung": "...",
  "tools": "...",
  "ziel": "..."
}
