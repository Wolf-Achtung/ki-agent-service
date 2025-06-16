# src/agents/json_agent.py
from crewai_tools import BaseAgent
import jsonschema

class JsonAgent(BaseAgent):
    def run(self, inputs):
        data = inputs.get("questionnaire", {})

        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "unternehmen": {"type": "string"},
                "datum": {"type": "string"},
            },
            "required": ["name", "unternehmen", "datum"]
        }

        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            return {"error": f"JSON-Fehler: {e.message}"}

        return {"cleaned": data}
