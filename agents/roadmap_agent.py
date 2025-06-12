def road_text(payload):
    from openai import OpenAI
    client = OpenAI()
    prompt = f"""Empfehle 3 konkrete Handlungsschritte für:
Score: {payload['score']} ({payload['status']}), Maßnahme: {payload['massnahmen']}, Herausforderung: {payload['herausforderung']}, Ziel: {payload['ziel']}."""
    res = client.chat.completions.create(model="gpt-4o", messages=[{"role":"user","content": prompt}])
    return res.choices[0].message.content
