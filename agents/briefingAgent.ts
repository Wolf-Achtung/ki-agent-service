import { createAgent } from "crewai";

export const briefingAgent = createAgent({
  name: "Briefing-Agent",
  role: "Analyst: KI-Geschäftsempfehlungen",
  prompt: `Nutze die Webhook-Daten (Fragebogen), um eine Management-Zusammenfassung ("executive_summary"), Analyse, Empfehlungen und Roadmap im JSON-Format zu erstellen. Berücksichtige Branche, Score, Herausforderungen, Tools und Ziel. Gib nur das JSON-Objekt zurück.`,
});
