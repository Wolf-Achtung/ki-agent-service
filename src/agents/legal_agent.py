# src/agents/legal_agent.py
from crewai_tools import BaseAgent

class LegalAgent(BaseAgent):
    def run(self, inputs):
        data = inputs.get("cleaned", {})
        unternehmen = data.get("unternehmen", "").lower()

        if "ai" in unternehmen or "gpt" in unternehmen:
            status = "⚠️ Rechtlicher Hinweis nötig"
            bewertung = "Bitte Datenschutz & Urheberrecht prüfen."
        else:
            status = "✅ Keine Risiken erkennbar"
            bewertung = "Standardprüfung ausreichend."

        return {
            "status": status,
            "bewertung": bewertung
        }
