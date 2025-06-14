// prompts/bewertung.ts

import type { KIInput } from "@/types";

export function buildBewertungsPrompt(input: KIInput) {
  return [
    {
      role: "system",
      content: "Du bist ein strategischer KI-Berater. Erzeuge anhand der Eingabedaten eine Bewertung mit konkreten Empfehlungen."
    },
    {
      role: "user",
      content: `Eingabe:\n${JSON.stringify(input)}`
    }
  ];
}
