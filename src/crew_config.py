from crewai_tools import Crew
from agents.json_agent import JsonAgent
from agents.legal_agent import LegalAgent
from agents.briefing_agent import BriefingAgent

crew = Crew(agents=[
    JsonAgent(),
    LegalAgent(),
    BriefingAgent()
])

