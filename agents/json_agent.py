from crewai import Agent

class JsonAgent(Agent):
    def __init__(self):
        super().__init__(
            name="JsonAgent",
            role="Extrahiert strukturierte JSON-Daten aus Freitext",
            goal="JSON aus unstrukturierten Textantworten generieren",
            backstory="Du bist ein Datenstrukturierer, spezialisiert auf textbasiertes Parsing.",
            verbose=True
        )

