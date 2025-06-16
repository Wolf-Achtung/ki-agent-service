from crewai import Crew
from .json_agent import JsonAgent
from .legal_agent import LegalAgent
from .briefing_agent import BriefingAgent

crew = Crew(agents=[
    JsonAgent(),
    LegalAgent(),
    BriefingAgent()
])
