def exec_text(payload):
    from openai import OpenAI
    client = OpenAI()
    prompt = f"""Du bist Senior KI-Analyst.
Branche: {payload['branche']}
Selbstständig: {payload['selbststaendig']}
Maßnahme: {payload['massnahmen']}
Score: {payload['score']} ({payload['status']})
Bewertung: {payload['bewertung']}
Herausforderung: {payload['herausforderung']}
Tools: {payload['tools']}
Ziel: {payload['ziel']}

Erstelle eine Executive Summary (ca. 1200 Zeichen)."""
    res = client.chat.completions.create(model="gpt-4o", messages=[{"role":"user","content": prompt}])
    return res.choices[0].message.content
