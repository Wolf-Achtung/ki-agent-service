// form.js – optimierte Version für Railway-Agentensystem

const form = document.getElementById("kiForm");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const formData = new FormData(form);

  // Branche
  let branche = formData.get("branche");
  if (branche === "Sonstige") {
    const sonstige = formData.get("branche_sonstige");
    branche = sonstige || "Sonstige";
  }

  // Multiplikator
  const multiplikatorMap = {
    "Medien": 1.1,
    "Bildung": 1.0,
    "Verwaltung": 0.9,
    "Handel": 1.0,
    "IT / Technologie": 1.2
  };
  const multiplikator = multiplikatorMap[branche] || 1.0;

  // Scoring
  const antworten = {};
  let score = 0;
  for (let i = 1; i <= 10; i++) {
    const val = formData.get(`frage${i}`);
    antworten[`frage${i}`] = val;
    score += parseInt(val || "0");
  }

  score = Math.round(score * multiplikator);

  // Bewertung
  let status = "Basis";
  let bewertung = "Erste Grundlagen vorhanden, weiter so!";
  if (score >= 27 && score <= 35) {
    status = "Fortgeschritten";
    bewertung = "Solide Umsetzung mit strategischem Potenzial.";
  } else if (score > 35) {
    status = "Exzellent";
    bewertung = "Sie gehören zu den Vorreitern beim KI-Einsatz.";
  }

  const heute = new Date();
  const datum = heute.toISOString().split("T")[0];
  const gueltig_bis = new Date(heute.setFullYear(heute.getFullYear() + 1)).toISOString().split("T")[0];

  // JSON-Payload
  const payload = {
    name: formData.get("name"),
    unternehmen: formData.get("unternehmen"),
    branche,
    selbststaendig: formData.get("selbststaendig"),
    massnahmen: formData.get("massnahmen"),
    herausforderung: formData.get("herausforderung"),
    tools: formData.get("tools"),
    ziel: formData.get("ziel"),
    antworten,
    score,
    status,
    bewertung,
    datum,
    gueltig_bis
  };

  console.log("🚀 Sende an KI-Agenten-API:", payload);

  fetch("https://ki-agent-service-production.up.railway.app/api/analyse", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
    .then((res) => {
      if (!res.ok) throw new Error("Fehler vom Server: " + res.status);
      return res.json();
    })
    .then(() => {
      window.location.href = "danke.html";
    })
    .catch((err) => {
      console.error("❌ Fehler beim API-Aufruf:", err);
      alert("Es gab ein Problem beim Senden der Daten. Bitte später erneut versuchen.");
    });
});
