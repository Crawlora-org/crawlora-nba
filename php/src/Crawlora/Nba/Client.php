<?php

declare(strict_types=1);

namespace Crawlora\Nba;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'nba';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 70;
    public const OPERATION_IDS = ["nba-box-score", "nba-box-score-advanced", "nba-box-score-defensive", "nba-box-score-four-factors", "nba-box-score-misc", "nba-box-score-player-track", "nba-box-score-scoring", "nba-box-score-summary", "nba-box-score-usage", "nba-common-all-players", "nba-draft-combine-anthro", "nba-enums", "nba-franchise-history", "nba-game-detail", "nba-games", "nba-homepage-leaders", "nba-homepage-v2", "nba-hustle-player", "nba-hustle-stats", "nba-hustle-team", "nba-league-game-log", "nba-lineup-shot-chart", "nba-lineups", "nba-news", "nba-opp-pt-shot", "nba-play-by-play", "nba-player-awards", "nba-player-bio-stats", "nba-player-career-stats", "nba-player-clutch", "nba-player-compare", "nba-player-dash-by-clutch", "nba-player-dash-by-game-splits", "nba-player-dash-by-last-n-games", "nba-player-dash-by-opponent", "nba-player-dash-pt-pass", "nba-player-dash-pt-reb", "nba-player-dash-pt-shots", "nba-player-game-logs", "nba-player-info", "nba-player-profile-v2", "nba-player-pt-shot", "nba-player-stats", "nba-player-streak-finder", "nba-players", "nba-playoff-picture", "nba-playoff-series", "nba-pt-defend", "nba-pt-stats", "nba-scoreboard", "nba-shot-chart", "nba-standings", "nba-synergy-play-types", "nba-team-dash-by-clutch", "nba-team-dash-by-game-splits", "nba-team-dash-by-last-n-games", "nba-team-dash-by-opponent", "nba-team-dash-pt-pass", "nba-team-dash-pt-reb", "nba-team-dash-pt-shots", "nba-team-details", "nba-team-game-logs", "nba-team-info-common", "nba-team-on-off", "nba-team-pt-shot", "nba-team-roster", "nba-team-shot-locations", "nba-team-stats", "nba-team-stats-leaders", "nba-team-years"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"nba-box-score": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "First period to include, 0 to 14; 0 means from the start example(0)", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end example(14)", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/box-score", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-box-score-advanced": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-advanced", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "First period to include, 0 to 14; 0 means from the start", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/box-score-advanced", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-box-score-defensive": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-defensive", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}], "path": "/nba/box-score-defensive", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-box-score-four-factors": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-four-factors", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "First period to include, 0 to 14; 0 means from the start", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/box-score-four-factors", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-box-score-misc": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-misc", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "First period to include, 0 to 14; 0 means from the start", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/box-score-misc", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-box-score-player-track": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-player-track", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}], "path": "/nba/box-score-player-track", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-box-score-scoring": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-scoring", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "First period to include, 0 to 14; 0 means from the start", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/box-score-scoring", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-box-score-summary": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-summary", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}], "path": "/nba/box-score-summary", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-box-score-usage": {"bodyParam": null, "bodyRequired": false, "id": "nba-box-score-usage", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "First period to include, 0 to 14; 0 means from the start", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/box-score-usage", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-common-all-players": {"bodyParam": null, "bodyRequired": false, "id": "nba-common-all-players", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "When true, only players on a current roster are returned", "in": "query", "name": "is_only_current_season", "type": "boolean"}], "path": "/nba/common-all-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "is_only_current_season", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "nba-draft-combine-anthro": {"bodyParam": null, "bodyRequired": false, "id": "nba-draft-combine-anthro", "method": "GET", "params": [{"description": "Four-digit draft year", "in": "query", "name": "season_year", "required": true, "type": "string", "x-example": "2025"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}], "path": "/nba/draft-combine-anthro", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "season_year", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-enums": {"bodyParam": null, "bodyRequired": false, "id": "nba-enums", "method": "GET", "params": [], "path": "/nba/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "nba-franchise-history": {"bodyParam": null, "bodyRequired": false, "id": "nba-franchise-history", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Optional team id from nba-standings; narrows the history to that franchise", "in": "query", "name": "team_id", "type": "integer", "x-example": 1610612741}], "path": "/nba/franchise-history", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "team_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-game-detail": {"bodyParam": null, "bodyRequired": false, "id": "nba-game-detail", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}], "path": "/nba/game-detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-games": {"bodyParam": null, "bodyRequired": false, "id": "nba-games", "method": "GET", "params": [], "path": "/nba/games", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "nba-homepage-leaders": {"bodyParam": null, "bodyRequired": false, "id": "nba-homepage-leaders", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Leader category", "enum": ["Points", "Rebounds"], "in": "query", "name": "stat_category", "type": "string", "x-example": "Points"}, {"description": "Subject", "enum": ["Team"], "in": "query", "name": "player_or_team", "type": "string", "x-example": "Team"}, {"description": "Player pool", "in": "query", "name": "player_scope", "type": "string", "x-example": "All Players"}, {"description": "Game window", "enum": ["Season"], "in": "query", "name": "game_scope", "type": "string", "x-example": "Season"}], "path": "/nba/homepage-leaders", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"enum": ["Points", "Rebounds"], "in": "query", "name": "stat_category", "type": "string"}, {"enum": ["Team"], "in": "query", "name": "player_or_team", "type": "string"}, {"in": "query", "name": "player_scope", "type": "string"}, {"enum": ["Season"], "in": "query", "name": "game_scope", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-homepage-v2": {"bodyParam": null, "bodyRequired": false, "id": "nba-homepage-v2", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Game window; only Season is verified", "enum": ["Season"], "in": "query", "name": "game_scope", "type": "string", "x-example": "Season"}, {"description": "Player pool; only All Players is verified", "in": "query", "name": "player_scope", "type": "string", "x-example": "All Players"}, {"description": "Subject; only Player is verified here", "enum": ["Player"], "in": "query", "name": "player_or_team", "type": "string", "x-example": "Player"}, {"description": "Statistic family; only Traditional is verified", "enum": ["Traditional"], "in": "query", "name": "stat_type", "type": "string", "x-example": "Traditional"}], "path": "/nba/homepage-v2", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["Season"], "in": "query", "name": "game_scope", "type": "string"}, {"in": "query", "name": "player_scope", "type": "string"}, {"enum": ["Player"], "in": "query", "name": "player_or_team", "type": "string"}, {"enum": ["Traditional"], "in": "query", "name": "stat_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-hustle-player": {"bodyParam": null, "bodyRequired": false, "id": "nba-hustle-player", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/hustle-player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-hustle-stats": {"bodyParam": null, "bodyRequired": false, "id": "nba-hustle-stats", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}], "path": "/nba/hustle-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-hustle-team": {"bodyParam": null, "bodyRequired": false, "id": "nba-hustle-team", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "path": "/nba/hustle-team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-league-game-log": {"bodyParam": null, "bodyRequired": false, "id": "nba-league-game-log", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Ordering; ASC or DESC", "enum": ["DESC"], "in": "query", "name": "direction", "type": "string", "x-example": "DESC"}, {"description": "T for one row per team, P for one row per player", "enum": ["T"], "in": "query", "name": "player_or_team", "type": "string", "x-example": "T"}, {"description": "Sort key; only DATE is verified", "enum": ["DATE"], "in": "query", "name": "sorter", "type": "string", "x-example": "DATE"}], "path": "/nba/league-game-log", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["DESC"], "in": "query", "name": "direction", "type": "string"}, {"enum": ["T"], "in": "query", "name": "player_or_team", "type": "string"}, {"enum": ["DATE"], "in": "query", "name": "sorter", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-lineup-shot-chart": {"bodyParam": null, "bodyRequired": false, "id": "nba-lineup-shot-chart", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612738}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Shot-chart base event", "enum": ["FGA", "FG_PCT"], "in": "query", "name": "context_measure", "type": "string", "x-example": "FG_PCT"}, {"description": "Lineup size; only 5 is verified", "enum": [5], "in": "query", "name": "group_quantity", "type": "integer", "x-example": 5}, {"description": "Period selector; 0 means the whole game", "in": "query", "name": "period", "type": "integer", "x-example": 0}], "path": "/nba/lineup-shot-chart", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["FGA", "FG_PCT"], "in": "query", "name": "context_measure", "type": "string"}, {"enum": ["5"], "in": "query", "name": "group_quantity", "type": "integer"}, {"in": "query", "name": "period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-lineups": {"bodyParam": null, "bodyRequired": false, "id": "nba-lineups", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Statistic family", "enum": ["Base"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Lineup size; only 5 is verified", "enum": [5], "in": "query", "name": "group_quantity", "type": "integer", "x-example": 5}], "path": "/nba/lineups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["Base"], "in": "query", "name": "measure_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["5"], "in": "query", "name": "group_quantity", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-news": {"bodyParam": null, "bodyRequired": false, "id": "nba-news", "method": "GET", "params": [], "path": "/nba/news", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "nba-opp-pt-shot": {"bodyParam": null, "bodyRequired": false, "id": "nba-opp-pt-shot", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "path": "/nba/opp-pt-shot", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-play-by-play": {"bodyParam": null, "bodyRequired": false, "id": "nba-play-by-play", "method": "GET", "params": [{"description": "Ten-digit game id from nba-scoreboard", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "0022600196"}, {"description": "First period to include, 0 to 14; 0 means from the start example(0)", "in": "query", "name": "start_period", "type": "integer", "x-example": 0}, {"description": "Last period to include, 0 to 14; 0 means through the end example(14)", "in": "query", "name": "end_period", "type": "integer", "x-example": 14}], "path": "/nba/play-by-play", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"in": "query", "name": "start_period", "type": "integer"}, {"in": "query", "name": "end_period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-player-awards": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-awards", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}], "path": "/nba/player-awards", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-player-bio-stats": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-bio-stats", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/player-bio-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-career-stats": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-career-stats", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "Aggregation; PerGame or Totals", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}], "path": "/nba/player-career-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-clutch": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-clutch", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"description": "Optional statistic family.", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}, {"description": "Optional clutch window; only 'Last 5 Minutes' is verified.", "enum": ["Last 5 Minutes"], "in": "query", "name": "clutch_time", "type": "string"}, {"description": "Optional score-margin filter; only 'Ahead or Behind' is verified.", "enum": ["Ahead or Behind"], "in": "query", "name": "ahead_behind", "type": "string"}, {"description": "Optional point margin; only 5 is verified.", "enum": [5], "in": "query", "name": "point_diff", "type": "integer"}], "path": "/nba/player-clutch", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}, {"enum": ["Last 5 Minutes"], "in": "query", "name": "clutch_time", "type": "string"}, {"enum": ["Ahead or Behind"], "in": "query", "name": "ahead_behind", "type": "string"}, {"enum": ["5"], "in": "query", "name": "point_diff", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-player-compare": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-compare", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Player ids for the left side; repeated or comma-separated", "in": "query", "items": {"type": "string"}, "name": "player_ids", "required": true, "type": "array", "x-example": "1628398"}, {"collectionFormat": "multi", "description": "Player ids for the right side; repeated or comma-separated", "in": "query", "items": {"type": "string"}, "name": "vs_player_ids", "required": true, "type": "array", "x-example": "2544"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/player-compare", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "player_ids", "required": true, "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "vs_player_ids", "required": true, "type": "array"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-by-clutch": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-by-clutch", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/player-dash-by-clutch", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-by-game-splits": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-by-game-splits", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/player-dash-by-game-splits", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-by-last-n-games": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-by-last-n-games", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/player-dash-by-last-n-games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-by-opponent": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-by-opponent", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/player-dash-by-opponent", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-pt-pass": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-pt-pass", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/player-dash-pt-pass", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-pt-reb": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-pt-reb", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/player-dash-pt-reb", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-dash-pt-shots": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-dash-pt-shots", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/player-dash-pt-shots", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-game-logs": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-game-logs", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Required player id from nba-players or nba-team-roster.", "in": "query", "name": "player_id", "required": true, "type": "integer"}], "path": "/nba/player-game-logs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-player-info": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-info", "method": "GET", "params": [{"description": "Player id from nba-players or nba-team-roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 1628398}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}], "path": "/nba/player-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-profile-v2": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-profile-v2", "method": "GET", "params": [{"description": "Required player id from nba-players or nba-team-roster.", "in": "query", "name": "player_id", "required": true, "type": "integer"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "path": "/nba/player-profile-v2", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "integer"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-pt-shot": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-pt-shot", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "path": "/nba/player-pt-shot", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-stats": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-stats", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type; Regular Season or Playoffs", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Statistic family; Base or Advanced", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}, {"description": "Aggregation; PerGame or Totals", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/player-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-player-streak-finder": {"bodyParam": null, "bodyRequired": false, "id": "nba-player-streak-finder", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional player id from nba-players; narrows the streaks to one player.", "in": "query", "name": "player_id", "type": "integer"}, {"description": "Optional minimum streak length in games.", "in": "query", "name": "min_games", "type": "integer"}], "path": "/nba/player-streak-finder", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"in": "query", "name": "player_id", "type": "integer"}, {"in": "query", "name": "min_games", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-players": {"bodyParam": null, "bodyRequired": false, "id": "nba-players", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Optional team id from nba-standings; narrows the index to that roster example(1610612741)", "in": "query", "name": "team_id", "type": "integer", "x-example": 1610612741}, {"description": "When true, keep only players active in the season", "in": "query", "name": "active", "type": "boolean"}], "path": "/nba/players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "team_id", "type": "integer"}, {"in": "query", "name": "active", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "nba-playoff-picture": {"bodyParam": null, "bodyRequired": false, "id": "nba-playoff-picture", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Five-digit season id such as 22026; defaults to the current season", "in": "query", "name": "season_id", "type": "string", "x-example": "22026"}], "path": "/nba/playoff-picture", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-playoff-series": {"bodyParam": null, "bodyRequired": false, "id": "nba-playoff-series", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}], "path": "/nba/playoff-series", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-pt-defend": {"bodyParam": null, "bodyRequired": false, "id": "nba-pt-defend", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Defended-shot category", "enum": ["Overall", "3 Pointers"], "in": "query", "name": "defense_category", "type": "string", "x-example": "Overall"}], "path": "/nba/pt-defend", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Overall", "3 Pointers"], "in": "query", "name": "defense_category", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-pt-stats": {"bodyParam": null, "bodyRequired": false, "id": "nba-pt-stats", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Tracking measure; only SpeedDistance is verified", "enum": ["SpeedDistance"], "in": "query", "name": "pt_measure_type", "type": "string", "x-example": "SpeedDistance"}], "path": "/nba/pt-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["SpeedDistance"], "in": "query", "name": "pt_measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-scoreboard": {"bodyParam": null, "bodyRequired": false, "id": "nba-scoreboard", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Game day in MM/DD/YYYY form; defaults to the current UTC date", "in": "query", "name": "game_date", "type": "string", "x-example": "11/08/2026"}, {"description": "Whole-day offset applied to the game day example(0)", "in": "query", "name": "day_offset", "type": "integer", "x-example": 0}], "path": "/nba/scoreboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "game_date", "type": "string"}, {"in": "query", "name": "day_offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-shot-chart": {"bodyParam": null, "bodyRequired": false, "id": "nba-shot-chart", "method": "GET", "params": [{"description": "Player id from nba-players; supply this or team_id", "in": "query", "name": "player_id", "type": "integer", "x-example": 1628398}, {"description": "Team id from nba-standings; supply this or player_id", "in": "query", "name": "team_id", "type": "integer"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Shot-chart base event", "enum": ["FGA", "FG_PCT"], "in": "query", "name": "context_measure", "type": "string", "x-example": "FGA"}], "path": "/nba/shot-chart", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "type": "integer"}, {"in": "query", "name": "team_id", "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["FGA", "FG_PCT"], "in": "query", "name": "context_measure", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-standings": {"bodyParam": null, "bodyRequired": false, "id": "nba-standings", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type; Regular Season or Playoffs", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}], "path": "/nba/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-synergy-play-types": {"bodyParam": null, "bodyRequired": false, "id": "nba-synergy-play-types", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Four-digit season year such as 2026; defaults to the current season", "in": "query", "name": "season_year", "type": "string", "x-example": "2026"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Synergy play type; only Isolation is verified", "enum": ["Isolation"], "in": "query", "name": "play_type", "type": "string", "x-example": "Isolation"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Subject", "enum": ["T"], "in": "query", "name": "player_or_team", "type": "string", "x-example": "T"}, {"description": "Grouping", "enum": ["offensive"], "in": "query", "name": "type_grouping", "type": "string", "x-example": "offensive"}], "path": "/nba/synergy-play-types", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season_year", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["Isolation"], "in": "query", "name": "play_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["T"], "in": "query", "name": "player_or_team", "type": "string"}, {"enum": ["offensive"], "in": "query", "name": "type_grouping", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-by-clutch": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-by-clutch", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612738}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/team-dash-by-clutch", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-by-game-splits": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-by-game-splits", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612738}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/team-dash-by-game-splits", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-by-last-n-games": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-by-last-n-games", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612738}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/team-dash-by-last-n-games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-by-opponent": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-by-opponent", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612738}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Statistic family; required upstream", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}], "path": "/nba/team-dash-by-opponent", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-pt-pass": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-pt-pass", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"description": "Required team id from nba-standings.", "in": "query", "name": "team_id", "required": true, "type": "integer"}], "path": "/nba/team-dash-pt-pass", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-pt-reb": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-pt-reb", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612738}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/team-dash-pt-reb", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-dash-pt-shots": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-dash-pt-shots", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"description": "Required team id from nba-standings.", "in": "query", "name": "team_id", "required": true, "type": "integer"}], "path": "/nba/team-dash-pt-shots", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-team-details": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-details", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612741}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}], "path": "/nba/team-details", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-game-logs": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-game-logs", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Required team id from nba-standings.", "in": "query", "name": "team_id", "required": true, "type": "integer"}], "path": "/nba/team-game-logs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-team-info-common": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-info-common", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Required team id from nba-standings.", "in": "query", "name": "team_id", "required": true, "type": "integer"}], "path": "/nba/team-info-common", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-team-on-off": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-on-off", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"description": "Optional statistic family.", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}, {"description": "Required team id from nba-standings.", "in": "query", "name": "team_id", "required": true, "type": "integer"}], "path": "/nba/team-on-off", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "nba-team-pt-shot": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-pt-shot", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"description": "Optional season in YYYY-YY form; defaults to the current NBA season.", "in": "query", "name": "season", "type": "string"}, {"description": "Optional season type.", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"description": "Optional aggregation.", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "path": "/nba/team-pt-shot", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-roster": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-roster", "method": "GET", "params": [{"description": "Team id from nba-standings", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1610612741}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}], "path": "/nba/team-roster", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-shot-locations": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-shot-locations", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type", "enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Statistic family", "enum": ["Base"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}, {"description": "Aggregation", "enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Distance bucket set; only By Zone is verified", "in": "query", "name": "distance_range", "type": "string", "x-example": "By Zone"}], "path": "/nba/team-shot-locations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["Base"], "in": "query", "name": "measure_type", "type": "string"}, {"enum": ["PerGame"], "in": "query", "name": "per_mode", "type": "string"}, {"in": "query", "name": "distance_range", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-stats": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-stats", "method": "GET", "params": [{"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type; Regular Season or Playoffs", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Statistic family; Base or Advanced", "enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string", "x-example": "Base"}, {"description": "Aggregation; PerGame or Totals", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}], "path": "/nba/team-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"], "in": "query", "name": "measure_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-stats-leaders": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-stats-leaders", "method": "GET", "params": [{"description": "Ranked statistic; PTS, REB or AST", "enum": ["PTS", "REB", "AST", "BLK", "STL", "TOV"], "in": "query", "name": "stat_category", "required": true, "type": "string", "x-example": "PTS"}, {"description": "League id; only 00 (NBA) is verified", "enum": ["00"], "in": "query", "name": "league_id", "type": "string", "x-example": "00"}, {"description": "Season in YYYY-YY form; defaults to the current NBA season", "in": "query", "name": "season", "type": "string", "x-example": "2026-27"}, {"description": "Season type; Regular Season or Playoffs", "enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string", "x-example": "Regular Season"}, {"description": "Aggregation; PerGame or Totals", "enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string", "x-example": "PerGame"}, {"description": "Player-pool scope; S is all players (the only verified value)", "enum": ["S"], "in": "query", "name": "scope", "type": "string", "x-example": "S"}], "path": "/nba/team-stats-leaders", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["PTS", "REB", "AST", "BLK", "STL", "TOV"], "in": "query", "name": "stat_category", "required": true, "type": "string"}, {"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "season", "type": "string"}, {"enum": ["Regular Season", "Playoffs", "Pre Season", "All Star"], "in": "query", "name": "season_type", "type": "string"}, {"enum": ["PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"], "in": "query", "name": "per_mode", "type": "string"}, {"enum": ["S"], "in": "query", "name": "scope", "type": "string"}], "security": ["ApiKeyAuth"]}, "nba-team-years": {"bodyParam": null, "bodyRequired": false, "id": "nba-team-years", "method": "GET", "params": [{"description": "Optional league id; only 00 (NBA) is verified.", "enum": ["00"], "in": "query", "name": "league_id", "type": "string"}], "path": "/nba/team-years", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["00"], "in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-nba-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function box_score(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score", $params, $responseType);
    }
    public function box_score_advanced(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-advanced", $params, $responseType);
    }
    public function box_score_defensive(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-defensive", $params, $responseType);
    }
    public function box_score_four_factors(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-four-factors", $params, $responseType);
    }
    public function box_score_misc(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-misc", $params, $responseType);
    }
    public function box_score_player_track(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-player-track", $params, $responseType);
    }
    public function box_score_scoring(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-scoring", $params, $responseType);
    }
    public function box_score_summary(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-summary", $params, $responseType);
    }
    public function box_score_usage(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-box-score-usage", $params, $responseType);
    }
    public function common_all_players(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-common-all-players", $params, $responseType);
    }
    public function draft_combine_anthro(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-draft-combine-anthro", $params, $responseType);
    }
    public function enums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-enums", $params, $responseType);
    }
    public function franchise_history(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-franchise-history", $params, $responseType);
    }
    public function game_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-game-detail", $params, $responseType);
    }
    public function games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-games", $params, $responseType);
    }
    public function homepage_leaders(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-homepage-leaders", $params, $responseType);
    }
    public function homepage_v2(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-homepage-v2", $params, $responseType);
    }
    public function hustle_player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-hustle-player", $params, $responseType);
    }
    public function hustle_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-hustle-stats", $params, $responseType);
    }
    public function hustle_team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-hustle-team", $params, $responseType);
    }
    public function league_game_log(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-league-game-log", $params, $responseType);
    }
    public function lineup_shot_chart(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-lineup-shot-chart", $params, $responseType);
    }
    public function lineups(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-lineups", $params, $responseType);
    }
    public function news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-news", $params, $responseType);
    }
    public function opp_pt_shot(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-opp-pt-shot", $params, $responseType);
    }
    public function play_by_play(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-play-by-play", $params, $responseType);
    }
    public function player_awards(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-awards", $params, $responseType);
    }
    public function player_bio_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-bio-stats", $params, $responseType);
    }
    public function player_career_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-career-stats", $params, $responseType);
    }
    public function player_clutch(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-clutch", $params, $responseType);
    }
    public function player_compare(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-compare", $params, $responseType);
    }
    public function player_dash_by_clutch(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-by-clutch", $params, $responseType);
    }
    public function player_dash_by_game_splits(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-by-game-splits", $params, $responseType);
    }
    public function player_dash_by_last_n_games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-by-last-n-games", $params, $responseType);
    }
    public function player_dash_by_opponent(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-by-opponent", $params, $responseType);
    }
    public function player_dash_pt_pass(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-pt-pass", $params, $responseType);
    }
    public function player_dash_pt_reb(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-pt-reb", $params, $responseType);
    }
    public function player_dash_pt_shots(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-dash-pt-shots", $params, $responseType);
    }
    public function player_game_logs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-game-logs", $params, $responseType);
    }
    public function player_info(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-info", $params, $responseType);
    }
    public function player_profile_v2(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-profile-v2", $params, $responseType);
    }
    public function player_pt_shot(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-pt-shot", $params, $responseType);
    }
    public function player_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-stats", $params, $responseType);
    }
    public function player_streak_finder(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-player-streak-finder", $params, $responseType);
    }
    public function players(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-players", $params, $responseType);
    }
    public function playoff_picture(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-playoff-picture", $params, $responseType);
    }
    public function playoff_series(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-playoff-series", $params, $responseType);
    }
    public function pt_defend(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-pt-defend", $params, $responseType);
    }
    public function pt_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-pt-stats", $params, $responseType);
    }
    public function scoreboard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-scoreboard", $params, $responseType);
    }
    public function shot_chart(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-shot-chart", $params, $responseType);
    }
    public function standings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-standings", $params, $responseType);
    }
    public function synergy_play_types(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-synergy-play-types", $params, $responseType);
    }
    public function team_dash_by_clutch(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-by-clutch", $params, $responseType);
    }
    public function team_dash_by_game_splits(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-by-game-splits", $params, $responseType);
    }
    public function team_dash_by_last_n_games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-by-last-n-games", $params, $responseType);
    }
    public function team_dash_by_opponent(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-by-opponent", $params, $responseType);
    }
    public function team_dash_pt_pass(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-pt-pass", $params, $responseType);
    }
    public function team_dash_pt_reb(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-pt-reb", $params, $responseType);
    }
    public function team_dash_pt_shots(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-dash-pt-shots", $params, $responseType);
    }
    public function team_details(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-details", $params, $responseType);
    }
    public function team_game_logs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-game-logs", $params, $responseType);
    }
    public function team_info_common(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-info-common", $params, $responseType);
    }
    public function team_on_off(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-on-off", $params, $responseType);
    }
    public function team_pt_shot(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-pt-shot", $params, $responseType);
    }
    public function team_roster(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-roster", $params, $responseType);
    }
    public function team_shot_locations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-shot-locations", $params, $responseType);
    }
    public function team_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-stats", $params, $responseType);
    }
    public function team_stats_leaders(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-stats-leaders", $params, $responseType);
    }
    public function team_years(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("nba-team-years", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
