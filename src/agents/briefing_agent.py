# src/agents/briefing_agent.py
from crewai_tools import BaseAgent
from datetime import datetime

class BriefingAgent(BaseAgent):
    def run(self, inputs):
        cleaned = inputs.get("cleaned", {})
        legal = inputs.get("status", "")
        bewertung = inputs.get("bewertung", "")

        return {
            "name": cleaned.get("name", ""),
            "unternehmen": cleaned.get("unternehmen", ""),
            "datum": cleaned.get("datum", str(datetime.now().date())),
            "score": 75,  # Beispielscore, kann dynamisch werden
            "status": legal,
            "bewertung": bewertung,
            "executive_summary": f"{cleaned.get('unternehmen')} wurde bewertet.",
            "analyse": "Weitere Daten fehlen – dies ist ein Basisbriefing."
        }
