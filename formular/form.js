const form = document.getElementById("kiForm");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const formData = new FormData(form);

  // 🏷 Branche
  let branche = formData.get("branche");
  if (branche === "Sonstiges") {
    const sonstige = formData.get("branche_sonstige");
    branche = sonstige || "Sonstige";
  }

  // 🔢 Multiplikator & Scoring
  const multiplikatorMap = {
    "Medien": 1.1,
    "Bildung": 1.3,
    "IT / Technologie": 1.5,
    "Handel": 0.9,
    "Industrie": 1.2,
    "Dienstleistung": 1.0
  };

  const multiplikator = multiplikatorMap[branche] || 1.0;

  let score = 0;
  let antworten = {};
  for (let i = 1; i <= 10; i++) {
    const antwort = formData.get(`frage${i}`);
    antworten[`frage${i}`] = antwort;
    score += parseInt(antwort || "0");
  }

  score = Math.round(score * multiplikator);

  // 🎯 Bewertung
  let status = "Basis";
  let bewertung = "Erste Grundlagen vorhanden, weiter so!";
  if (score >= 27 && score <= 35) {
    status = "Fortgeschritten";
    bewertung = "Solide Umsetzung mit strategischem Potenzial.";
  } else if (score > 35) {
    status = "Exzellent";
    bewertung = "Sie gehören zu den Vorreitern beim KI-Einsatz.";
  }

  // 📆 Datum & Ausblick
  const heute = new Date();
  const datum = heute.toISOString().split("T")[0];
  const quvis_bis = new Date(heute.setFullYear(heute.getFullYear() + 1)).toISOString().split("T")[0];

  // 🧠 KI-Analyse als Text
  const analyseText = `
    Branche: ${branche}
    Selbstständig: ${formData.get("selbststaendig")}
    Tools: ${formData.get("tools")}
    Maßnahmen: ${formData.get("massnahmen")}
    Ziel: ${formData.get("ziel")}
    Herausforderung: ${formData.get("herausforderung")}
    Antworten: ${Object.entries(antworten).map(([k, v]) => `${k}: ${v}`).join(", ")}
    Score: ${score}
    Bewertung: ${bewertung}
    Status: ${status}
    Datum: ${datum}, QuVis bis: ${quvis_bis}
  `.trim();

  // 📦 Finaler Payload
  const payload = {
    name: formData.get("name"),
    unternehmen: formData.get("unternehmen"),
    analyseInput: analyseText,
    score,
    bewertung,
    status,
    datum,
    quvis_bis
  };

  console.log("📦 Sende an KI-Agenten:", payload);

  // 📡 API-Aufruf
  fetch("https://ki-agent-service-production.up.railway.app/analyse", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
    .then((res) => {
      if (!res.ok) throw new Error("Serverfehler: " + res.status);
      return res.json();
    })
    .then(() => {
      window.location.href = "danke.html";
    })
    .catch((err) => {
      console.error("❌ Fehler beim Senden:", err);
      alert("Es gab ein Problem beim Senden. Bitte später erneut versuchen.");
    });
});
