from fastapi import FastAPI, Request
from agents.executive_agent import exec_text
from agents.strategy_agent import strat_text
from agents.roadmap_agent import road_text
from agents.resource_agent import resource_text
from agents.merge_agent import merge_sections
import requests
import os

app = FastAPI()

@app.post("/submit")
async def submit_briefing(req: Request):
    payload = await req.json()
    exec_sec = exec_text(payload)
    strat_sec = strat_text(payload)
    road_sec = road_text(payload)
    res_sec = resource_text(payload)
    full = merge_sections(exec_sec, strat_sec, road_sec, res_sec)

    # Weiterleitung an Make Webhook
    make_url = os.getenv("MAKE_WEBHOOK_URL")
  # Setze das in Railway!
    requests.post(make_url, json=full)

    return {"status": "ok", "briefing": full}
