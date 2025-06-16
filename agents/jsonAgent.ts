import { createAgent } from "crewai";

export const jsonAgent = createAgent({
  name: "JSON-Agent",
  role: "Technischer Formatter",
  prompt: `Kombiniere die bisherigen JSON-Antworten. Stelle sicher, dass alle Pflichtfelder vorhanden und valide formatiert sind. Felder: executive_summary, analyse, empfehlung1/2/3, roadmap, ressourcen, zukunft, risikoprofil, tooltipps, foerdertipps, branchenvergleich, trendreport, visionaer. Gib nur reines JSON zurück.`,
});