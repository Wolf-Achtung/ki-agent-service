import { config } from 'dotenv';
config();
import { OpenAI } from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! });

async function run() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: 'Was ist ein KI-Agent?' }],
    model: 'gpt-4',
  });
  console.log(completion.choices[0].message.content);
}

run();
