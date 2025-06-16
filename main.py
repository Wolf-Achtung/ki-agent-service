from agents.crew_config import crew
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def run_crew(request: Request):
    body = await request.json()
    result = crew.run({"questionnaire": body})
    return {"result": result}
