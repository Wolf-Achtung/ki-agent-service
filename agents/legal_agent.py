from crewai import Agent

class LegalAgent(Agent):
    def __init__(self):
        super().__init__(
            name="LegalAgent",
            role="Bewertet rechtliche Risiken",
            goal="Juristische Implikationen aus dem Text analysieren",
            backstory="Du bist ein juristischer KI-Analyst mit Fokus auf Datenschutz und KI-Recht.",
            verbose=True
        )
