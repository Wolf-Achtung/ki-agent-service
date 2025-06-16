from crewai import Agent

class JsonAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Analytischer Daten-Parser",
            goal="Strukturiere Fragebogen-Antworten in verwertbares JSON",
            backstory="Du bist spezialisiert auf Scoring und Datenstrukturierung bei Managementumfragen.",
            verbose=True
        )
