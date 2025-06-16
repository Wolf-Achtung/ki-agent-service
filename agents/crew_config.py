from crewai import Crew, Task
from .json_agent import JsonAgent
from .legal_agent import LegalAgent
from .briefing_agent import BriefingAgent

# Agenten instanziieren
json_agent = JsonAgent()
legal_agent = LegalAgent()
briefing_agent = BriefingAgent()

# Aufgaben (Tasks) mit Prompt-Logik
json_task = Task(
    agent=json_agent,
    description="Analysiere die folgenden Fragebogen-Antworten und wandle sie in strukturierte JSON-Daten mit Score, Status und Empfehlung um. Gehe systematisch vor.",
    expected_output="Ein JSON-Objekt mit score, status, bewertung, und antworten"
)

legal_task = Task(
    agent=legal_agent,
    description="Analysiere die Antwortdaten im Hinblick auf Datenschutz und rechtliche Anforderungen bei KI-Einführung. Fasse Risiken und Empfehlungen prägnant zusammen.",
    expected_output="Kurze rechtliche Einschätzung (max. 5 Sätze)"
)

briefing_task = Task(
    agent=briefing_agent,
    description="Erzeuge ein strategisches Briefing für die Unternehmensleitung basierend auf den Ausgaben der anderen Agenten. Fasse Stärken, Schwächen, Chancen, rechtliche Punkte und Handlungsoptionen zusammen.",
    expected_output="Ein HTML-formatierter Text für ein PDF-Dokument"
)

# Crew mit Aufgaben
crew = Crew(
    agents=[json_agent, legal_agent, briefing_agent],
    tasks=[json_task, legal_task, briefing_task]
)