import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class NBAClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-nba-js/0.1.0" });
    this["boxScore"] = (...args) => this.request("nba-box-score", ...args);
    this["boxScoreAdvanced"] = (...args) => this.request("nba-box-score-advanced", ...args);
    this["boxScoreDefensive"] = (...args) => this.request("nba-box-score-defensive", ...args);
    this["boxScoreFourFactors"] = (...args) => this.request("nba-box-score-four-factors", ...args);
    this["boxScoreMisc"] = (...args) => this.request("nba-box-score-misc", ...args);
    this["boxScorePlayerTrack"] = (...args) => this.request("nba-box-score-player-track", ...args);
    this["boxScoreScoring"] = (...args) => this.request("nba-box-score-scoring", ...args);
    this["boxScoreSummary"] = (...args) => this.request("nba-box-score-summary", ...args);
    this["boxScoreUsage"] = (...args) => this.request("nba-box-score-usage", ...args);
    this["commonAllPlayers"] = (...args) => this.request("nba-common-all-players", ...args);
    this["draftCombineAnthro"] = (...args) => this.request("nba-draft-combine-anthro", ...args);
    this["enums"] = (...args) => this.request("nba-enums", ...args);
    this["franchiseHistory"] = (...args) => this.request("nba-franchise-history", ...args);
    this["gameDetail"] = (...args) => this.request("nba-game-detail", ...args);
    this["games"] = (...args) => this.request("nba-games", ...args);
    this["homepageLeaders"] = (...args) => this.request("nba-homepage-leaders", ...args);
    this["homepageV2"] = (...args) => this.request("nba-homepage-v2", ...args);
    this["hustlePlayer"] = (...args) => this.request("nba-hustle-player", ...args);
    this["hustleStats"] = (...args) => this.request("nba-hustle-stats", ...args);
    this["hustleTeam"] = (...args) => this.request("nba-hustle-team", ...args);
    this["leagueGameLog"] = (...args) => this.request("nba-league-game-log", ...args);
    this["lineupShotChart"] = (...args) => this.request("nba-lineup-shot-chart", ...args);
    this["lineups"] = (...args) => this.request("nba-lineups", ...args);
    this["news"] = (...args) => this.request("nba-news", ...args);
    this["oppPtShot"] = (...args) => this.request("nba-opp-pt-shot", ...args);
    this["playByPlay"] = (...args) => this.request("nba-play-by-play", ...args);
    this["playerAwards"] = (...args) => this.request("nba-player-awards", ...args);
    this["playerBioStats"] = (...args) => this.request("nba-player-bio-stats", ...args);
    this["playerCareerStats"] = (...args) => this.request("nba-player-career-stats", ...args);
    this["playerClutch"] = (...args) => this.request("nba-player-clutch", ...args);
    this["playerCompare"] = (...args) => this.request("nba-player-compare", ...args);
    this["playerDashByClutch"] = (...args) => this.request("nba-player-dash-by-clutch", ...args);
    this["playerDashByGameSplits"] = (...args) => this.request("nba-player-dash-by-game-splits", ...args);
    this["playerDashByLastNGames"] = (...args) => this.request("nba-player-dash-by-last-n-games", ...args);
    this["playerDashByOpponent"] = (...args) => this.request("nba-player-dash-by-opponent", ...args);
    this["playerDashPtPass"] = (...args) => this.request("nba-player-dash-pt-pass", ...args);
    this["playerDashPtReb"] = (...args) => this.request("nba-player-dash-pt-reb", ...args);
    this["playerDashPtShots"] = (...args) => this.request("nba-player-dash-pt-shots", ...args);
    this["playerGameLogs"] = (...args) => this.request("nba-player-game-logs", ...args);
    this["playerInfo"] = (...args) => this.request("nba-player-info", ...args);
    this["playerProfileV2"] = (...args) => this.request("nba-player-profile-v2", ...args);
    this["playerPtShot"] = (...args) => this.request("nba-player-pt-shot", ...args);
    this["playerStats"] = (...args) => this.request("nba-player-stats", ...args);
    this["playerStreakFinder"] = (...args) => this.request("nba-player-streak-finder", ...args);
    this["players"] = (...args) => this.request("nba-players", ...args);
    this["playoffPicture"] = (...args) => this.request("nba-playoff-picture", ...args);
    this["playoffSeries"] = (...args) => this.request("nba-playoff-series", ...args);
    this["ptDefend"] = (...args) => this.request("nba-pt-defend", ...args);
    this["ptStats"] = (...args) => this.request("nba-pt-stats", ...args);
    this["scoreboard"] = (...args) => this.request("nba-scoreboard", ...args);
    this["shotChart"] = (...args) => this.request("nba-shot-chart", ...args);
    this["standings"] = (...args) => this.request("nba-standings", ...args);
    this["synergyPlayTypes"] = (...args) => this.request("nba-synergy-play-types", ...args);
    this["teamDashByClutch"] = (...args) => this.request("nba-team-dash-by-clutch", ...args);
    this["teamDashByGameSplits"] = (...args) => this.request("nba-team-dash-by-game-splits", ...args);
    this["teamDashByLastNGames"] = (...args) => this.request("nba-team-dash-by-last-n-games", ...args);
    this["teamDashByOpponent"] = (...args) => this.request("nba-team-dash-by-opponent", ...args);
    this["teamDashPtPass"] = (...args) => this.request("nba-team-dash-pt-pass", ...args);
    this["teamDashPtReb"] = (...args) => this.request("nba-team-dash-pt-reb", ...args);
    this["teamDashPtShots"] = (...args) => this.request("nba-team-dash-pt-shots", ...args);
    this["teamDetails"] = (...args) => this.request("nba-team-details", ...args);
    this["teamGameLogs"] = (...args) => this.request("nba-team-game-logs", ...args);
    this["teamInfoCommon"] = (...args) => this.request("nba-team-info-common", ...args);
    this["teamOnOff"] = (...args) => this.request("nba-team-on-off", ...args);
    this["teamPtShot"] = (...args) => this.request("nba-team-pt-shot", ...args);
    this["teamRoster"] = (...args) => this.request("nba-team-roster", ...args);
    this["teamShotLocations"] = (...args) => this.request("nba-team-shot-locations", ...args);
    this["teamStats"] = (...args) => this.request("nba-team-stats", ...args);
    this["teamStatsLeaders"] = (...args) => this.request("nba-team-stats-leaders", ...args);
    this["teamYears"] = (...args) => this.request("nba-team-years", ...args);
  }
}

export { NBAClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default NBAClient;
