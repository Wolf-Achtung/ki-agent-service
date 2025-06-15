// form.js – finale Version mit Bewertungslogik & sauberem Payload

const form = document.getElementById("kiForm");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const formData = new FormData(form);

  // 1. Einstellungen
  const selbststaendig = formData.get("selbststaendig") === "ja";
  const branche = formData.get("branche") || "Allgemein";

  const multiplikatorMap = {
    "Medien": 1.1,
    "Bildung": 1.0,
    "Verwaltung": 0.9,
    "Handel": 1.0,
    "IT / Software": 1.2
  };
  const multiplikator = multiplikatorMap[branche] || 1.0;

  // 2. Antworten sammeln
  const antworten = {};
  let score = 0;

  for (let i = 1; i <= 10; i++) {
    const val = formData.get(`q${i}`);
    antworten[`q${i}`] = val;

    if (val === "ja") score += 3;
    else if (val === "teilweise / geplant") score += 2;
    else if (val === "nein") score += 1;
  }

  score = Math.round(score * multiplikator);
  if (selbststaendig && score < 30) score += 2;

  // 3. Status & Bewertung
  let status = "Basis";
  let bewertung = "Erste Grundlagen vorhanden, weiter so!";
  let badge_url = "https://example.com/badge-basis.png";

  if (score >= 27 && score <= 35) {
    status = "Fortgeschritten";
    bewertung = "Solide Umsetzung mit strategischem Potenzial.";
    badge_url = "https://example.com/badge-fortgeschritten.png";
  } else if (score > 35) {
    status = "Exzellent";
    bewertung = "Sie gehören zu den Vorreitern beim KI-Einsatz.";
    badge_url = "https://example.com/badge-exzellent.png";
  }

  // 4. Datum & Gültigkeit
  const heute = new Date();
  const datum = heute.toISOString().split("T")[0];
  const gueltig_bis = new Date(heute.setFullYear(heute.getFullYear() + 1)).toISOString().split("T")[0];

  // 5. JSON-Payload
  const payload = {
    unternehmen: formData.get("unternehmen"),
    name: formData.get("name"),
    branche: branche,
    selbststaendig: selbststaendig ? "Ja" : "Nein",
    massnahmen: formData.get("massnahmen"),
    score: score,
    status: status,
    bewertung: bewertung,
    herausforderung: formData.get("herausforderung"),
    tools: formData.get("tools"),
    ziel: formData.get("ziel"),
    datum: datum,
    gueltig_bis: gueltig_bis,
    antworten: antworten,
    branchenbeschreibung: "" // Platzhalter – wird später im Agenten ergänzt
  };

  // Debug
  console.log("📤 Sende an Make:", payload);

  // 6. Senden an Make Webhook
fetch("https://ki-agent-service-production-a3fc.up.railway.app/submit", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
  })
    .then((response) => {
      if (!response.ok) throw new Error("Fehler beim Übertragen: " + response.status);
      return response.json().catch(() => ({}));
    })
    .then(() => {
      window.location.href = "danke.html";
    })
    .catch((error) => {
      console.error("❌ Fehler beim Senden:", error);
      alert("Fehler beim Senden der Daten. Details in der Konsole.");
    });
});
