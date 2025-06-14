// agent/index.ts

import type { KIInput } from "@/types";
import { bewertungsAgent } from "@/agents/bewertungs-agent";

export async function runAgent(input: KIInput) {
  return await bewertungsAgent(input);
}
