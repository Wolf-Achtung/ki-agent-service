def resource_text(payload):
    from openai import OpenAI
    client = OpenAI()
    prompt = f"""Nenne Tools, Förderprogramme und Best Practices:
Branche: {payload['branche']}, Ziel: {payload['ziel']}."""
    res = client.chat.completions.create(model="gpt-4o", messages=[{"role":"user","content": prompt}])
    return res.choices[0].message.content
