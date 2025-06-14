// agents/bewertungs-agent.ts

import { OpenAIClient } from "@/lib/openai";
import { buildBewertungsPrompt } from "@/prompts/bewertung";
import type { KIInput, BewertungOutput } from "@/types";

export async function bewertungsAgent(input: KIInput): Promise<BewertungOutput> {
  const messages = buildBewertungsPrompt(input);
  const response = await OpenAIClient.chat({
    model: "gpt-4", messages
  });
  // Wenn Ausgabe gültiges JSON
  return JSON.parse(response);
}
