from crewai import Agent

class LegalAgent(Agent):
    def __init__(self):
        super().__init__(
            role="KI-Compliance-Berater",
            goal="Bewerte rechtliche Risiken aus den Antworten",
            backstory="Du bist Experte für Datenschutzrecht und KI-Regulierung im europäischen Raum.",
            verbose=True
        )
