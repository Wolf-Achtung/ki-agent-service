import { createAgent } from "crewai";

export const legalAgent = createAgent({
  name: "Legal-Agent",
  role: "Experte für Datenschutz und EU AI Act",
  prompt: `Bewerte das KI-Vorhaben in Bezug auf Risiken, EU AI Act und DSGVO. Ergänze die JSON-Struktur mit einem "risikoprofil" (Risiko-Klasse, Begründung, Pflichten) und "foerdertipps" (Programm, Zielgruppe, Nutzen). Gib nur das JSON-Objekt zurück.`,
});
