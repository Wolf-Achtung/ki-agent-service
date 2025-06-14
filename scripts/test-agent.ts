import { runAgent } from "@/agent";

const input = {
  unternehmen: "Muster GmbH",
  name: "Max Mustermann",
  branche: "IT",
  score: 85
};

runAgent(input).then(console.log).catch(console.error);
