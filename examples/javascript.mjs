import { NBAClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new NBAClient({ apiKey });

  const games = await client.games({  });
  console.log("games", games);
  const enums = await client.enums({  });
  console.log("enums", enums);
