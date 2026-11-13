import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class NBAClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScore(params: OperationParamsMap["nba-box-score"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreAdvanced(params: OperationParamsMap["nba-box-score-advanced"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreDefensive(params: OperationParamsMap["nba-box-score-defensive"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreFourFactors(params: OperationParamsMap["nba-box-score-four-factors"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreMisc(params: OperationParamsMap["nba-box-score-misc"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScorePlayerTrack(params: OperationParamsMap["nba-box-score-player-track"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreScoring(params: OperationParamsMap["nba-box-score-scoring"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreSummary(params: OperationParamsMap["nba-box-score-summary"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  boxScoreUsage(params: OperationParamsMap["nba-box-score-usage"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  commonAllPlayers(params?: OperationParamsMap["nba-common-all-players"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  draftCombineAnthro(params: OperationParamsMap["nba-draft-combine-anthro"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  enums(params?: OperationParamsMap["nba-enums"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  franchiseHistory(params?: OperationParamsMap["nba-franchise-history"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gameDetail(params: OperationParamsMap["nba-game-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  games(params?: OperationParamsMap["nba-games"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  homepageLeaders(params?: OperationParamsMap["nba-homepage-leaders"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  homepageV2(params?: OperationParamsMap["nba-homepage-v2"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hustlePlayer(params?: OperationParamsMap["nba-hustle-player"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hustleStats(params: OperationParamsMap["nba-hustle-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hustleTeam(params?: OperationParamsMap["nba-hustle-team"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagueGameLog(params?: OperationParamsMap["nba-league-game-log"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lineupShotChart(params: OperationParamsMap["nba-lineup-shot-chart"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lineups(params?: OperationParamsMap["nba-lineups"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params?: OperationParamsMap["nba-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  oppPtShot(params?: OperationParamsMap["nba-opp-pt-shot"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playByPlay(params: OperationParamsMap["nba-play-by-play"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerAwards(params: OperationParamsMap["nba-player-awards"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerBioStats(params?: OperationParamsMap["nba-player-bio-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerCareerStats(params: OperationParamsMap["nba-player-career-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerClutch(params?: OperationParamsMap["nba-player-clutch"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerCompare(params: OperationParamsMap["nba-player-compare"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashByClutch(params: OperationParamsMap["nba-player-dash-by-clutch"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashByGameSplits(params: OperationParamsMap["nba-player-dash-by-game-splits"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashByLastNGames(params: OperationParamsMap["nba-player-dash-by-last-n-games"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashByOpponent(params: OperationParamsMap["nba-player-dash-by-opponent"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashPtPass(params: OperationParamsMap["nba-player-dash-pt-pass"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashPtReb(params: OperationParamsMap["nba-player-dash-pt-reb"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerDashPtShots(params: OperationParamsMap["nba-player-dash-pt-shots"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerGameLogs(params: OperationParamsMap["nba-player-game-logs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerInfo(params: OperationParamsMap["nba-player-info"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerProfileV2(params: OperationParamsMap["nba-player-profile-v2"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerPtShot(params?: OperationParamsMap["nba-player-pt-shot"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerStats(params?: OperationParamsMap["nba-player-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerStreakFinder(params?: OperationParamsMap["nba-player-streak-finder"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  players(params?: OperationParamsMap["nba-players"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playoffPicture(params?: OperationParamsMap["nba-playoff-picture"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playoffSeries(params?: OperationParamsMap["nba-playoff-series"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  ptDefend(params?: OperationParamsMap["nba-pt-defend"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  ptStats(params?: OperationParamsMap["nba-pt-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scoreboard(params?: OperationParamsMap["nba-scoreboard"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  shotChart(params?: OperationParamsMap["nba-shot-chart"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  standings(params?: OperationParamsMap["nba-standings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  synergyPlayTypes(params?: OperationParamsMap["nba-synergy-play-types"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashByClutch(params: OperationParamsMap["nba-team-dash-by-clutch"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashByGameSplits(params: OperationParamsMap["nba-team-dash-by-game-splits"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashByLastNGames(params: OperationParamsMap["nba-team-dash-by-last-n-games"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashByOpponent(params: OperationParamsMap["nba-team-dash-by-opponent"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashPtPass(params: OperationParamsMap["nba-team-dash-pt-pass"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashPtReb(params: OperationParamsMap["nba-team-dash-pt-reb"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDashPtShots(params: OperationParamsMap["nba-team-dash-pt-shots"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamDetails(params: OperationParamsMap["nba-team-details"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamGameLogs(params: OperationParamsMap["nba-team-game-logs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamInfoCommon(params: OperationParamsMap["nba-team-info-common"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamOnOff(params: OperationParamsMap["nba-team-on-off"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamPtShot(params?: OperationParamsMap["nba-team-pt-shot"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamRoster(params: OperationParamsMap["nba-team-roster"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamShotLocations(params?: OperationParamsMap["nba-team-shot-locations"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamStats(params?: OperationParamsMap["nba-team-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamStatsLeaders(params: OperationParamsMap["nba-team-stats-leaders"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamYears(params?: OperationParamsMap["nba-team-years"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScore(params: OperationParamsMap["nba-box-score"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreAdvanced(params: OperationParamsMap["nba-box-score-advanced"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreDefensive(params: OperationParamsMap["nba-box-score-defensive"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreFourFactors(params: OperationParamsMap["nba-box-score-four-factors"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreMisc(params: OperationParamsMap["nba-box-score-misc"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScorePlayerTrack(params: OperationParamsMap["nba-box-score-player-track"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreScoring(params: OperationParamsMap["nba-box-score-scoring"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreSummary(params: OperationParamsMap["nba-box-score-summary"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  boxScoreUsage(params: OperationParamsMap["nba-box-score-usage"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  commonAllPlayers(params?: OperationParamsMap["nba-common-all-players"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  draftCombineAnthro(params: OperationParamsMap["nba-draft-combine-anthro"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  enums(params?: OperationParamsMap["nba-enums"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  franchiseHistory(params?: OperationParamsMap["nba-franchise-history"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gameDetail(params: OperationParamsMap["nba-game-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  games(params?: OperationParamsMap["nba-games"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  homepageLeaders(params?: OperationParamsMap["nba-homepage-leaders"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  homepageV2(params?: OperationParamsMap["nba-homepage-v2"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hustlePlayer(params?: OperationParamsMap["nba-hustle-player"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hustleStats(params: OperationParamsMap["nba-hustle-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hustleTeam(params?: OperationParamsMap["nba-hustle-team"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagueGameLog(params?: OperationParamsMap["nba-league-game-log"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lineupShotChart(params: OperationParamsMap["nba-lineup-shot-chart"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lineups(params?: OperationParamsMap["nba-lineups"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params?: OperationParamsMap["nba-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  oppPtShot(params?: OperationParamsMap["nba-opp-pt-shot"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playByPlay(params: OperationParamsMap["nba-play-by-play"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerAwards(params: OperationParamsMap["nba-player-awards"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerBioStats(params?: OperationParamsMap["nba-player-bio-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerCareerStats(params: OperationParamsMap["nba-player-career-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerClutch(params?: OperationParamsMap["nba-player-clutch"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerCompare(params: OperationParamsMap["nba-player-compare"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashByClutch(params: OperationParamsMap["nba-player-dash-by-clutch"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashByGameSplits(params: OperationParamsMap["nba-player-dash-by-game-splits"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashByLastNGames(params: OperationParamsMap["nba-player-dash-by-last-n-games"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashByOpponent(params: OperationParamsMap["nba-player-dash-by-opponent"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashPtPass(params: OperationParamsMap["nba-player-dash-pt-pass"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashPtReb(params: OperationParamsMap["nba-player-dash-pt-reb"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerDashPtShots(params: OperationParamsMap["nba-player-dash-pt-shots"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerGameLogs(params: OperationParamsMap["nba-player-game-logs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerInfo(params: OperationParamsMap["nba-player-info"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerProfileV2(params: OperationParamsMap["nba-player-profile-v2"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerPtShot(params?: OperationParamsMap["nba-player-pt-shot"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerStats(params?: OperationParamsMap["nba-player-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerStreakFinder(params?: OperationParamsMap["nba-player-streak-finder"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  players(params?: OperationParamsMap["nba-players"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playoffPicture(params?: OperationParamsMap["nba-playoff-picture"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playoffSeries(params?: OperationParamsMap["nba-playoff-series"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  ptDefend(params?: OperationParamsMap["nba-pt-defend"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  ptStats(params?: OperationParamsMap["nba-pt-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scoreboard(params?: OperationParamsMap["nba-scoreboard"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  shotChart(params?: OperationParamsMap["nba-shot-chart"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  standings(params?: OperationParamsMap["nba-standings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  synergyPlayTypes(params?: OperationParamsMap["nba-synergy-play-types"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashByClutch(params: OperationParamsMap["nba-team-dash-by-clutch"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashByGameSplits(params: OperationParamsMap["nba-team-dash-by-game-splits"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashByLastNGames(params: OperationParamsMap["nba-team-dash-by-last-n-games"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashByOpponent(params: OperationParamsMap["nba-team-dash-by-opponent"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashPtPass(params: OperationParamsMap["nba-team-dash-pt-pass"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashPtReb(params: OperationParamsMap["nba-team-dash-pt-reb"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDashPtShots(params: OperationParamsMap["nba-team-dash-pt-shots"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamDetails(params: OperationParamsMap["nba-team-details"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamGameLogs(params: OperationParamsMap["nba-team-game-logs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamInfoCommon(params: OperationParamsMap["nba-team-info-common"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamOnOff(params: OperationParamsMap["nba-team-on-off"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamPtShot(params?: OperationParamsMap["nba-team-pt-shot"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamRoster(params: OperationParamsMap["nba-team-roster"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamShotLocations(params?: OperationParamsMap["nba-team-shot-locations"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamStats(params?: OperationParamsMap["nba-team-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamStatsLeaders(params: OperationParamsMap["nba-team-stats-leaders"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamYears(params?: OperationParamsMap["nba-team-years"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  boxScore(...args: OperationRequestArgs<"nba-box-score">): Promise<OperationResponseMap["nba-box-score"]>;
  boxScoreAdvanced(...args: OperationRequestArgs<"nba-box-score-advanced">): Promise<OperationResponseMap["nba-box-score-advanced"]>;
  boxScoreDefensive(...args: OperationRequestArgs<"nba-box-score-defensive">): Promise<OperationResponseMap["nba-box-score-defensive"]>;
  boxScoreFourFactors(...args: OperationRequestArgs<"nba-box-score-four-factors">): Promise<OperationResponseMap["nba-box-score-four-factors"]>;
  boxScoreMisc(...args: OperationRequestArgs<"nba-box-score-misc">): Promise<OperationResponseMap["nba-box-score-misc"]>;
  boxScorePlayerTrack(...args: OperationRequestArgs<"nba-box-score-player-track">): Promise<OperationResponseMap["nba-box-score-player-track"]>;
  boxScoreScoring(...args: OperationRequestArgs<"nba-box-score-scoring">): Promise<OperationResponseMap["nba-box-score-scoring"]>;
  boxScoreSummary(...args: OperationRequestArgs<"nba-box-score-summary">): Promise<OperationResponseMap["nba-box-score-summary"]>;
  boxScoreUsage(...args: OperationRequestArgs<"nba-box-score-usage">): Promise<OperationResponseMap["nba-box-score-usage"]>;
  commonAllPlayers(...args: OperationRequestArgs<"nba-common-all-players">): Promise<OperationResponseMap["nba-common-all-players"]>;
  draftCombineAnthro(...args: OperationRequestArgs<"nba-draft-combine-anthro">): Promise<OperationResponseMap["nba-draft-combine-anthro"]>;
  enums(...args: OperationRequestArgs<"nba-enums">): Promise<OperationResponseMap["nba-enums"]>;
  franchiseHistory(...args: OperationRequestArgs<"nba-franchise-history">): Promise<OperationResponseMap["nba-franchise-history"]>;
  gameDetail(...args: OperationRequestArgs<"nba-game-detail">): Promise<OperationResponseMap["nba-game-detail"]>;
  games(...args: OperationRequestArgs<"nba-games">): Promise<OperationResponseMap["nba-games"]>;
  homepageLeaders(...args: OperationRequestArgs<"nba-homepage-leaders">): Promise<OperationResponseMap["nba-homepage-leaders"]>;
  homepageV2(...args: OperationRequestArgs<"nba-homepage-v2">): Promise<OperationResponseMap["nba-homepage-v2"]>;
  hustlePlayer(...args: OperationRequestArgs<"nba-hustle-player">): Promise<OperationResponseMap["nba-hustle-player"]>;
  hustleStats(...args: OperationRequestArgs<"nba-hustle-stats">): Promise<OperationResponseMap["nba-hustle-stats"]>;
  hustleTeam(...args: OperationRequestArgs<"nba-hustle-team">): Promise<OperationResponseMap["nba-hustle-team"]>;
  leagueGameLog(...args: OperationRequestArgs<"nba-league-game-log">): Promise<OperationResponseMap["nba-league-game-log"]>;
  lineupShotChart(...args: OperationRequestArgs<"nba-lineup-shot-chart">): Promise<OperationResponseMap["nba-lineup-shot-chart"]>;
  lineups(...args: OperationRequestArgs<"nba-lineups">): Promise<OperationResponseMap["nba-lineups"]>;
  news(...args: OperationRequestArgs<"nba-news">): Promise<OperationResponseMap["nba-news"]>;
  oppPtShot(...args: OperationRequestArgs<"nba-opp-pt-shot">): Promise<OperationResponseMap["nba-opp-pt-shot"]>;
  playByPlay(...args: OperationRequestArgs<"nba-play-by-play">): Promise<OperationResponseMap["nba-play-by-play"]>;
  playerAwards(...args: OperationRequestArgs<"nba-player-awards">): Promise<OperationResponseMap["nba-player-awards"]>;
  playerBioStats(...args: OperationRequestArgs<"nba-player-bio-stats">): Promise<OperationResponseMap["nba-player-bio-stats"]>;
  playerCareerStats(...args: OperationRequestArgs<"nba-player-career-stats">): Promise<OperationResponseMap["nba-player-career-stats"]>;
  playerClutch(...args: OperationRequestArgs<"nba-player-clutch">): Promise<OperationResponseMap["nba-player-clutch"]>;
  playerCompare(...args: OperationRequestArgs<"nba-player-compare">): Promise<OperationResponseMap["nba-player-compare"]>;
  playerDashByClutch(...args: OperationRequestArgs<"nba-player-dash-by-clutch">): Promise<OperationResponseMap["nba-player-dash-by-clutch"]>;
  playerDashByGameSplits(...args: OperationRequestArgs<"nba-player-dash-by-game-splits">): Promise<OperationResponseMap["nba-player-dash-by-game-splits"]>;
  playerDashByLastNGames(...args: OperationRequestArgs<"nba-player-dash-by-last-n-games">): Promise<OperationResponseMap["nba-player-dash-by-last-n-games"]>;
  playerDashByOpponent(...args: OperationRequestArgs<"nba-player-dash-by-opponent">): Promise<OperationResponseMap["nba-player-dash-by-opponent"]>;
  playerDashPtPass(...args: OperationRequestArgs<"nba-player-dash-pt-pass">): Promise<OperationResponseMap["nba-player-dash-pt-pass"]>;
  playerDashPtReb(...args: OperationRequestArgs<"nba-player-dash-pt-reb">): Promise<OperationResponseMap["nba-player-dash-pt-reb"]>;
  playerDashPtShots(...args: OperationRequestArgs<"nba-player-dash-pt-shots">): Promise<OperationResponseMap["nba-player-dash-pt-shots"]>;
  playerGameLogs(...args: OperationRequestArgs<"nba-player-game-logs">): Promise<OperationResponseMap["nba-player-game-logs"]>;
  playerInfo(...args: OperationRequestArgs<"nba-player-info">): Promise<OperationResponseMap["nba-player-info"]>;
  playerProfileV2(...args: OperationRequestArgs<"nba-player-profile-v2">): Promise<OperationResponseMap["nba-player-profile-v2"]>;
  playerPtShot(...args: OperationRequestArgs<"nba-player-pt-shot">): Promise<OperationResponseMap["nba-player-pt-shot"]>;
  playerStats(...args: OperationRequestArgs<"nba-player-stats">): Promise<OperationResponseMap["nba-player-stats"]>;
  playerStreakFinder(...args: OperationRequestArgs<"nba-player-streak-finder">): Promise<OperationResponseMap["nba-player-streak-finder"]>;
  players(...args: OperationRequestArgs<"nba-players">): Promise<OperationResponseMap["nba-players"]>;
  playoffPicture(...args: OperationRequestArgs<"nba-playoff-picture">): Promise<OperationResponseMap["nba-playoff-picture"]>;
  playoffSeries(...args: OperationRequestArgs<"nba-playoff-series">): Promise<OperationResponseMap["nba-playoff-series"]>;
  ptDefend(...args: OperationRequestArgs<"nba-pt-defend">): Promise<OperationResponseMap["nba-pt-defend"]>;
  ptStats(...args: OperationRequestArgs<"nba-pt-stats">): Promise<OperationResponseMap["nba-pt-stats"]>;
  scoreboard(...args: OperationRequestArgs<"nba-scoreboard">): Promise<OperationResponseMap["nba-scoreboard"]>;
  shotChart(...args: OperationRequestArgs<"nba-shot-chart">): Promise<OperationResponseMap["nba-shot-chart"]>;
  standings(...args: OperationRequestArgs<"nba-standings">): Promise<OperationResponseMap["nba-standings"]>;
  synergyPlayTypes(...args: OperationRequestArgs<"nba-synergy-play-types">): Promise<OperationResponseMap["nba-synergy-play-types"]>;
  teamDashByClutch(...args: OperationRequestArgs<"nba-team-dash-by-clutch">): Promise<OperationResponseMap["nba-team-dash-by-clutch"]>;
  teamDashByGameSplits(...args: OperationRequestArgs<"nba-team-dash-by-game-splits">): Promise<OperationResponseMap["nba-team-dash-by-game-splits"]>;
  teamDashByLastNGames(...args: OperationRequestArgs<"nba-team-dash-by-last-n-games">): Promise<OperationResponseMap["nba-team-dash-by-last-n-games"]>;
  teamDashByOpponent(...args: OperationRequestArgs<"nba-team-dash-by-opponent">): Promise<OperationResponseMap["nba-team-dash-by-opponent"]>;
  teamDashPtPass(...args: OperationRequestArgs<"nba-team-dash-pt-pass">): Promise<OperationResponseMap["nba-team-dash-pt-pass"]>;
  teamDashPtReb(...args: OperationRequestArgs<"nba-team-dash-pt-reb">): Promise<OperationResponseMap["nba-team-dash-pt-reb"]>;
  teamDashPtShots(...args: OperationRequestArgs<"nba-team-dash-pt-shots">): Promise<OperationResponseMap["nba-team-dash-pt-shots"]>;
  teamDetails(...args: OperationRequestArgs<"nba-team-details">): Promise<OperationResponseMap["nba-team-details"]>;
  teamGameLogs(...args: OperationRequestArgs<"nba-team-game-logs">): Promise<OperationResponseMap["nba-team-game-logs"]>;
  teamInfoCommon(...args: OperationRequestArgs<"nba-team-info-common">): Promise<OperationResponseMap["nba-team-info-common"]>;
  teamOnOff(...args: OperationRequestArgs<"nba-team-on-off">): Promise<OperationResponseMap["nba-team-on-off"]>;
  teamPtShot(...args: OperationRequestArgs<"nba-team-pt-shot">): Promise<OperationResponseMap["nba-team-pt-shot"]>;
  teamRoster(...args: OperationRequestArgs<"nba-team-roster">): Promise<OperationResponseMap["nba-team-roster"]>;
  teamShotLocations(...args: OperationRequestArgs<"nba-team-shot-locations">): Promise<OperationResponseMap["nba-team-shot-locations"]>;
  teamStats(...args: OperationRequestArgs<"nba-team-stats">): Promise<OperationResponseMap["nba-team-stats"]>;
  teamStatsLeaders(...args: OperationRequestArgs<"nba-team-stats-leaders">): Promise<OperationResponseMap["nba-team-stats-leaders"]>;
  teamYears(...args: OperationRequestArgs<"nba-team-years">): Promise<OperationResponseMap["nba-team-years"]>;
}
export { NBAClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default NBAClient;
