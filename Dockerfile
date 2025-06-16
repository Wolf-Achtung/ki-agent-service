# Basis-Image
FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /app

# Requirements kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Restlichen Code kopieren
COPY . .

# Port-Umgebungsvariable (Railway setzt PORT)
ENV PORT=8080

# App starten mit uvicorn auf Port 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]






