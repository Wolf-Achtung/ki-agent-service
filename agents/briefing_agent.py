from crewai import Agent

class BriefingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="BriefingAgent",
            role="Fasst den Inhalt zusammen",
            goal="Erstellt ein Executive Briefing aus allen Agenten-Ergebnissen",
            backstory="Du bist spezialisiert auf Management-kompatible Zusammenfassungen.",
            verbose=True
        )
