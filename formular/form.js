// form.js – finale Version mit Bewertungslogik & Übergabe an Make

const form = document.getElementById("kiForm");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const formData = new FormData(form);

  // Bewertung nach Branche
  const branchenMultiplikator = {
    "Medien": 1.1,
    "Bildung": 1.0,
    "Verwaltung": 0.9,
    "Handel": 1.0,
    "IT / Software": 1.2
  };

  const selbststaendig = formData.get("selbststaendig") === "ja";
  const branche = formData.get("branche") || "Allgemein";
  const multiplikator = branchenMultiplikator[branche] || 1.0;

  // Score berechnen
  let score = 0;
  for (let i = 1; i <= 10; i++) {
    const value = formData.get(`q${i}`);
    if (value === "ja") score += 3;
    else if (value === "teilweise / geplant") score += 2;
    else if (value === "nein") score += 1;
  }

  score = Math.round(score * multiplikator);
  if (selbststaendig && score < 30) score += 2;

  // Status & Bewertung bestimmen
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

  // Datum vorbereiten
  const heute = new Date();
  const datum = heute.toISOString().split("T")[0];
  const gueltig_bis = new Date(heute.setFullYear(heute.getFullYear() + 1)).toISOString().split("T")[0];

  // Nutzdaten zusammenstellen
  const payload = {
    unternehmen: formData.get("unternehmen"),
    name: formData.get("name"),
    branche: branche,
    selbststaendig: selbststaendig ? "Ja" : "Nein",
    massnahmen: formData.get("massnahmen"),
    score: score,
    bewertung: bewertung,
    status: status,
    badge_url: badge_url,
    herausforderung: formData.get("herausforderung"),
    tools: formData.get("tools"),
    ziel: formData.get("ziel"),
    datum: datum,
    gueltig_bis: gueltig_bis
  };

  // Debug-Ausgabe
  console.log("📤 JSON an Make:", payload);

  // Abschicken an Make
  fetch("https://hook.eu2.make.com/kuupzg3nxvpy5xm84zb7j8pmrcon2r2r", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
    .then((response) => {
      if (!response.ok) throw new Error("Fehler beim Übertragen: " + response.status);
      return response.json().catch(() => ({}));
    })
    .then(() => {
      alert("✅ Daten erfolgreich übermittelt.");
    })
    .catch((error) => {
      console.error("❌ Fehler beim Senden:", error);
      alert("Fehler beim Senden der Daten. Details in der Konsole.");
    });
});
