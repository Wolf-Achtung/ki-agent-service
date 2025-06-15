import { Crew } from "crewai";
import { briefingAgent } from "../agents/briefingAgent";
import { legalAgent } from "../agents/legalAgent";
import { jsonAgent } from "../agents/jsonAgent";

export const crew = new Crew({
  agents: [briefingAgent, legalAgent, jsonAgent],
  autobridge: true,
  verbose: true
});
