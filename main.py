from fastapi import FastAPI, Request
from agents.executive_agent import exec_text
from agents.strategy_agent import strat_text
from agents.roadmap_agent import road_text
from agents.resource_agent import resource_text
from agents.merge_agent import merge_sections
import os, uvicorn

app = FastAPI()

@app.post("/briefing")
async def create_briefing(req: Request):
    payload = await req.json()
    exec_sec = exec_text(payload)
    strat_sec = strat_text(payload)
    road_sec = road_text(payload)
    res_sec = resource_text(payload)
    full = merge_sections(exec_sec, strat_sec, road_sec, res_sec)
    return {"briefing": full}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
