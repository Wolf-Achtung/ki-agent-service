import express from "express";
import dotenv from "dotenv";
import { crew } from "./crewConfig.js";
import fetch from "node-fetch";

dotenv.config();

const app = express();
app.use(express.json());

app.post("/webhook", async (req, res) => {
  const input = req.body;
  const result = await crew.run({ questionnaire: input });

  // optional: sende JSON direkt an PDFMonkey
  await fetch("https://api.pdfmonkey.io/api/v1/documents", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${process.env.PDFMONKEY_API_KEY}`
    },
    body: JSON.stringify({
      document: {
        template_id: "template-id-dein-pdf-briefing",
        payload: { briefingData: result }
      }
    })
  });

  res.json(result);
});

app.listen(process.env.PORT || 3000);
