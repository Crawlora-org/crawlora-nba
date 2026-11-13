import { NBAClient } from "../src/index.js";

const client = new NBAClient({ apiKey: "test-key" });
void client.boxScore({"game_id": "sample"});
void client.request("nba-box-score", {"game_id": "sample"});
const streamResponse: Promise<Response> = client.request("nba-box-score", {"game_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("nba-box-score", {"game_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.boxScore({"game_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("nba-box-score", {"game_id": "sample", "league_id": "00", "start_period": 1, "end_period": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("nba-box-score", {"game_id": "sample"}, { responseType: "text" });
void rawText;


void client.commonAllPlayers();
void client.request("nba-common-all-players");
// @ts-expect-error The selected operation requires its documented params.
void client.boxScore();
