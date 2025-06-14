// types.ts

export interface KIInput {
  unternehmen: string;
  name: string;
  branche: string;
  score: number;
  // ggf. weitere Feldanforderungen
}

export interface BewertungOutput {
  executive_summary: string;
  analyse: string;
  empfehlung1: { titel: string; beschreibung: string; next_step: string; tool: string };
  // ... weitere Felder analog Template
}
