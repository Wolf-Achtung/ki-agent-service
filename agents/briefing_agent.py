from crewai import Agent

class BriefingAgent(Agent):
    def __init__(self):
        super().__init__(
            role="KI-Strategie-Entwickler",
            goal="Erstelle ein Executive Briefing für Entscheider",
            backstory="Du verdichtest komplexe Analyseergebnisse zu umsetzbaren Management-Briefings.",
            verbose=True
        )

