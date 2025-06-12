def strat_text(payload):
    from openai import OpenAI
    client = OpenAI()
    prompt = f"""Analysiere basierend auf:
Branche: {payload['branche']}, Score: {payload['score']} ({payload['status']}), Maßnahme: {payload['massnahmen']}, Ziel: {payload['ziel']}
Generiere eine strategische Analyse (~1500 Zeichen)."""
    res = client.chat.completions.create(model="gpt-4o", messages=[{"role":"user","content": prompt}])
    return res.choices[0].message.content

