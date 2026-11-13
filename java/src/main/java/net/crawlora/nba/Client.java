package net.crawlora.nba;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the NBA endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 70;
    public static final List<String> OPERATION_IDS = List.of(
            "nba-box-score",
            "nba-box-score-advanced",
            "nba-box-score-defensive",
            "nba-box-score-four-factors",
            "nba-box-score-misc",
            "nba-box-score-player-track",
            "nba-box-score-scoring",
            "nba-box-score-summary",
            "nba-box-score-usage",
            "nba-common-all-players",
            "nba-draft-combine-anthro",
            "nba-enums",
            "nba-franchise-history",
            "nba-game-detail",
            "nba-games",
            "nba-homepage-leaders",
            "nba-homepage-v2",
            "nba-hustle-player",
            "nba-hustle-stats",
            "nba-hustle-team",
            "nba-league-game-log",
            "nba-lineup-shot-chart",
            "nba-lineups",
            "nba-news",
            "nba-opp-pt-shot",
            "nba-play-by-play",
            "nba-player-awards",
            "nba-player-bio-stats",
            "nba-player-career-stats",
            "nba-player-clutch",
            "nba-player-compare",
            "nba-player-dash-by-clutch",
            "nba-player-dash-by-game-splits",
            "nba-player-dash-by-last-n-games",
            "nba-player-dash-by-opponent",
            "nba-player-dash-pt-pass",
            "nba-player-dash-pt-reb",
            "nba-player-dash-pt-shots",
            "nba-player-game-logs",
            "nba-player-info",
            "nba-player-profile-v2",
            "nba-player-pt-shot",
            "nba-player-stats",
            "nba-player-streak-finder",
            "nba-players",
            "nba-playoff-picture",
            "nba-playoff-series",
            "nba-pt-defend",
            "nba-pt-stats",
            "nba-scoreboard",
            "nba-shot-chart",
            "nba-standings",
            "nba-synergy-play-types",
            "nba-team-dash-by-clutch",
            "nba-team-dash-by-game-splits",
            "nba-team-dash-by-last-n-games",
            "nba-team-dash-by-opponent",
            "nba-team-dash-pt-pass",
            "nba-team-dash-pt-reb",
            "nba-team-dash-pt-shots",
            "nba-team-details",
            "nba-team-game-logs",
            "nba-team-info-common",
            "nba-team-on-off",
            "nba-team-pt-shot",
            "nba-team-roster",
            "nba-team-shot-locations",
            "nba-team-stats",
            "nba-team-stats-leaders",
            "nba-team-years"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("nba-box-score", new Operation("nba-box-score", "GET", "/nba/box-score", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-advanced", new Operation("nba-box-score-advanced", "GET", "/nba/box-score-advanced", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-defensive", new Operation("nba-box-score-defensive", "GET", "/nba/box-score-defensive", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-four-factors", new Operation("nba-box-score-four-factors", "GET", "/nba/box-score-four-factors", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-misc", new Operation("nba-box-score-misc", "GET", "/nba/box-score-misc", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-player-track", new Operation("nba-box-score-player-track", "GET", "/nba/box-score-player-track", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-scoring", new Operation("nba-box-score-scoring", "GET", "/nba/box-score-scoring", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-summary", new Operation("nba-box-score-summary", "GET", "/nba/box-score-summary", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-box-score-usage", new Operation("nba-box-score-usage", "GET", "/nba/box-score-usage", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-common-all-players", new Operation("nba-common-all-players", "GET", "/nba/common-all-players", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("is_only_current_season", new Param("is_only_current_season", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-draft-combine-anthro", new Operation("nba-draft-combine-anthro", "GET", "/nba/draft-combine-anthro", Map.ofEntries(Map.entry("season_year", new Param("season_year", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv"))), List.of("application/json")));
        operations.put("nba-enums", new Operation("nba-enums", "GET", "/nba/enums", Map.of(), List.of("application/json")));
        operations.put("nba-franchise-history", new Operation("nba-franchise-history", "GET", "/nba/franchise-history", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-game-detail", new Operation("nba-game-detail", "GET", "/nba/game-detail", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-games", new Operation("nba-games", "GET", "/nba/games", Map.of(), List.of("application/json")));
        operations.put("nba-homepage-leaders", new Operation("nba-homepage-leaders", "GET", "/nba/homepage-leaders", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("stat_category", new Param("stat_category", "query", false, "string", List.of("Points", "Rebounds"), "csv")), Map.entry("player_or_team", new Param("player_or_team", "query", false, "string", List.of("Team"), "csv")), Map.entry("player_scope", new Param("player_scope", "query", false, "string", List.of(), "csv")), Map.entry("game_scope", new Param("game_scope", "query", false, "string", List.of("Season"), "csv"))), List.of("application/json")));
        operations.put("nba-homepage-v2", new Operation("nba-homepage-v2", "GET", "/nba/homepage-v2", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("game_scope", new Param("game_scope", "query", false, "string", List.of("Season"), "csv")), Map.entry("player_scope", new Param("player_scope", "query", false, "string", List.of(), "csv")), Map.entry("player_or_team", new Param("player_or_team", "query", false, "string", List.of("Player"), "csv")), Map.entry("stat_type", new Param("stat_type", "query", false, "string", List.of("Traditional"), "csv"))), List.of("application/json")));
        operations.put("nba-hustle-player", new Operation("nba-hustle-player", "GET", "/nba/hustle-player", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv"))), List.of("application/json")));
        operations.put("nba-hustle-stats", new Operation("nba-hustle-stats", "GET", "/nba/hustle-stats", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-hustle-team", new Operation("nba-hustle-team", "GET", "/nba/hustle-team", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-league-game-log", new Operation("nba-league-game-log", "GET", "/nba/league-game-log", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("DESC"), "csv")), Map.entry("player_or_team", new Param("player_or_team", "query", false, "string", List.of("T"), "csv")), Map.entry("sorter", new Param("sorter", "query", false, "string", List.of("DATE"), "csv"))), List.of("application/json")));
        operations.put("nba-lineup-shot-chart", new Operation("nba-lineup-shot-chart", "GET", "/nba/lineup-shot-chart", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("context_measure", new Param("context_measure", "query", false, "string", List.of("FGA", "FG_PCT"), "csv")), Map.entry("group_quantity", new Param("group_quantity", "query", false, "integer", List.of("5"), "csv")), Map.entry("period", new Param("period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-lineups", new Operation("nba-lineups", "GET", "/nba/lineups", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("group_quantity", new Param("group_quantity", "query", false, "integer", List.of("5"), "csv"))), List.of("application/json")));
        operations.put("nba-news", new Operation("nba-news", "GET", "/nba/news", Map.of(), List.of("application/json")));
        operations.put("nba-opp-pt-shot", new Operation("nba-opp-pt-shot", "GET", "/nba/opp-pt-shot", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-play-by-play", new Operation("nba-play-by-play", "GET", "/nba/play-by-play", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("start_period", new Param("start_period", "query", false, "integer", List.of(), "csv")), Map.entry("end_period", new Param("end_period", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-player-awards", new Operation("nba-player-awards", "GET", "/nba/player-awards", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-player-bio-stats", new Operation("nba-player-bio-stats", "GET", "/nba/player-bio-stats", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv"))), List.of("application/json")));
        operations.put("nba-player-career-stats", new Operation("nba-player-career-stats", "GET", "/nba/player-career-stats", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv"))), List.of("application/json")));
        operations.put("nba-player-clutch", new Operation("nba-player-clutch", "GET", "/nba/player-clutch", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv")), Map.entry("clutch_time", new Param("clutch_time", "query", false, "string", List.of("Last 5 Minutes"), "csv")), Map.entry("ahead_behind", new Param("ahead_behind", "query", false, "string", List.of("Ahead or Behind"), "csv")), Map.entry("point_diff", new Param("point_diff", "query", false, "integer", List.of("5"), "csv"))), List.of("application/json")));
        operations.put("nba-player-compare", new Operation("nba-player-compare", "GET", "/nba/player-compare", Map.ofEntries(Map.entry("player_ids", new Param("player_ids", "query", true, "array", List.of(), "multi")), Map.entry("vs_player_ids", new Param("vs_player_ids", "query", true, "array", List.of(), "multi")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-by-clutch", new Operation("nba-player-dash-by-clutch", "GET", "/nba/player-dash-by-clutch", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-by-game-splits", new Operation("nba-player-dash-by-game-splits", "GET", "/nba/player-dash-by-game-splits", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-by-last-n-games", new Operation("nba-player-dash-by-last-n-games", "GET", "/nba/player-dash-by-last-n-games", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-by-opponent", new Operation("nba-player-dash-by-opponent", "GET", "/nba/player-dash-by-opponent", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-pt-pass", new Operation("nba-player-dash-pt-pass", "GET", "/nba/player-dash-pt-pass", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-pt-reb", new Operation("nba-player-dash-pt-reb", "GET", "/nba/player-dash-pt-reb", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv"))), List.of("application/json")));
        operations.put("nba-player-dash-pt-shots", new Operation("nba-player-dash-pt-shots", "GET", "/nba/player-dash-pt-shots", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv"))), List.of("application/json")));
        operations.put("nba-player-game-logs", new Operation("nba-player-game-logs", "GET", "/nba/player-game-logs", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-player-info", new Operation("nba-player-info", "GET", "/nba/player-info", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv"))), List.of("application/json")));
        operations.put("nba-player-profile-v2", new Operation("nba-player-profile-v2", "GET", "/nba/player-profile-v2", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-player-pt-shot", new Operation("nba-player-pt-shot", "GET", "/nba/player-pt-shot", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-player-stats", new Operation("nba-player-stats", "GET", "/nba/player-stats", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-player-streak-finder", new Operation("nba-player-streak-finder", "GET", "/nba/player-streak-finder", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("player_id", new Param("player_id", "query", false, "integer", List.of(), "csv")), Map.entry("min_games", new Param("min_games", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-players", new Operation("nba-players", "GET", "/nba/players", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "integer", List.of(), "csv")), Map.entry("active", new Param("active", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-playoff-picture", new Operation("nba-playoff-picture", "GET", "/nba/playoff-picture", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season_id", new Param("season_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-playoff-series", new Operation("nba-playoff-series", "GET", "/nba/playoff-series", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-pt-defend", new Operation("nba-pt-defend", "GET", "/nba/pt-defend", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("defense_category", new Param("defense_category", "query", false, "string", List.of("Overall", "3 Pointers"), "csv"))), List.of("application/json")));
        operations.put("nba-pt-stats", new Operation("nba-pt-stats", "GET", "/nba/pt-stats", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("pt_measure_type", new Param("pt_measure_type", "query", false, "string", List.of("SpeedDistance"), "csv"))), List.of("application/json")));
        operations.put("nba-scoreboard", new Operation("nba-scoreboard", "GET", "/nba/scoreboard", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("game_date", new Param("game_date", "query", false, "string", List.of(), "csv")), Map.entry("day_offset", new Param("day_offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-shot-chart", new Operation("nba-shot-chart", "GET", "/nba/shot-chart", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", false, "integer", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("context_measure", new Param("context_measure", "query", false, "string", List.of("FGA", "FG_PCT"), "csv"))), List.of("application/json")));
        operations.put("nba-standings", new Operation("nba-standings", "GET", "/nba/standings", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv"))), List.of("application/json")));
        operations.put("nba-synergy-play-types", new Operation("nba-synergy-play-types", "GET", "/nba/synergy-play-types", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season_year", new Param("season_year", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("play_type", new Param("play_type", "query", false, "string", List.of("Isolation"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("player_or_team", new Param("player_or_team", "query", false, "string", List.of("T"), "csv")), Map.entry("type_grouping", new Param("type_grouping", "query", false, "string", List.of("offensive"), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-by-clutch", new Operation("nba-team-dash-by-clutch", "GET", "/nba/team-dash-by-clutch", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-by-game-splits", new Operation("nba-team-dash-by-game-splits", "GET", "/nba/team-dash-by-game-splits", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-by-last-n-games", new Operation("nba-team-dash-by-last-n-games", "GET", "/nba/team-dash-by-last-n-games", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-by-opponent", new Operation("nba-team-dash-by-opponent", "GET", "/nba/team-dash-by-opponent", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-pt-pass", new Operation("nba-team-dash-pt-pass", "GET", "/nba/team-dash-pt-pass", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-pt-reb", new Operation("nba-team-dash-pt-reb", "GET", "/nba/team-dash-pt-reb", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv"))), List.of("application/json")));
        operations.put("nba-team-dash-pt-shots", new Operation("nba-team-dash-pt-shots", "GET", "/nba/team-dash-pt-shots", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-details", new Operation("nba-team-details", "GET", "/nba/team-details", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv"))), List.of("application/json")));
        operations.put("nba-team-game-logs", new Operation("nba-team-game-logs", "GET", "/nba/team-game-logs", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-info-common", new Operation("nba-team-info-common", "GET", "/nba/team-info-common", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-on-off", new Operation("nba-team-on-off", "GET", "/nba/team-on-off", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-pt-shot", new Operation("nba-team-pt-shot", "GET", "/nba/team-pt-shot", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-team-roster", new Operation("nba-team-roster", "GET", "/nba/team-roster", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-shot-locations", new Operation("nba-team-shot-locations", "GET", "/nba/team-shot-locations", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame"), "csv")), Map.entry("distance_range", new Param("distance_range", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("nba-team-stats", new Operation("nba-team-stats", "GET", "/nba/team-stats", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("measure_type", new Param("measure_type", "query", false, "string", List.of("Base", "Advanced", "Misc", "Scoring", "Defense", "Opponent"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv"))), List.of("application/json")));
        operations.put("nba-team-stats-leaders", new Operation("nba-team-stats-leaders", "GET", "/nba/team-stats-leaders", Map.ofEntries(Map.entry("stat_category", new Param("stat_category", "query", true, "string", List.of("PTS", "REB", "AST", "BLK", "STL", "TOV"), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("season_type", new Param("season_type", "query", false, "string", List.of("Regular Season", "Playoffs", "Pre Season", "All Star"), "csv")), Map.entry("per_mode", new Param("per_mode", "query", false, "string", List.of("PerGame", "Totals", "Per36", "Per48", "Per100Possessions", "MinutesPer", "PerPossession"), "csv")), Map.entry("scope", new Param("scope", "query", false, "string", List.of("S"), "csv"))), List.of("application/json")));
        operations.put("nba-team-years", new Operation("nba-team-years", "GET", "/nba/team-years", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", false, "string", List.of("00"), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown NBA operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object boxScore(Map<String, ?> params) { return request("nba-box-score", params); }
    public Object boxScoreAdvanced(Map<String, ?> params) { return request("nba-box-score-advanced", params); }
    public Object boxScoreDefensive(Map<String, ?> params) { return request("nba-box-score-defensive", params); }
    public Object boxScoreFourFactors(Map<String, ?> params) { return request("nba-box-score-four-factors", params); }
    public Object boxScoreMisc(Map<String, ?> params) { return request("nba-box-score-misc", params); }
    public Object boxScorePlayerTrack(Map<String, ?> params) { return request("nba-box-score-player-track", params); }
    public Object boxScoreScoring(Map<String, ?> params) { return request("nba-box-score-scoring", params); }
    public Object boxScoreSummary(Map<String, ?> params) { return request("nba-box-score-summary", params); }
    public Object boxScoreUsage(Map<String, ?> params) { return request("nba-box-score-usage", params); }
    public Object commonAllPlayers(Map<String, ?> params) { return request("nba-common-all-players", params); }
    public Object draftCombineAnthro(Map<String, ?> params) { return request("nba-draft-combine-anthro", params); }
    public Object enums(Map<String, ?> params) { return request("nba-enums", params); }
    public Object franchiseHistory(Map<String, ?> params) { return request("nba-franchise-history", params); }
    public Object gameDetail(Map<String, ?> params) { return request("nba-game-detail", params); }
    public Object games(Map<String, ?> params) { return request("nba-games", params); }
    public Object homepageLeaders(Map<String, ?> params) { return request("nba-homepage-leaders", params); }
    public Object homepageV2(Map<String, ?> params) { return request("nba-homepage-v2", params); }
    public Object hustlePlayer(Map<String, ?> params) { return request("nba-hustle-player", params); }
    public Object hustleStats(Map<String, ?> params) { return request("nba-hustle-stats", params); }
    public Object hustleTeam(Map<String, ?> params) { return request("nba-hustle-team", params); }
    public Object leagueGameLog(Map<String, ?> params) { return request("nba-league-game-log", params); }
    public Object lineupShotChart(Map<String, ?> params) { return request("nba-lineup-shot-chart", params); }
    public Object lineups(Map<String, ?> params) { return request("nba-lineups", params); }
    public Object news(Map<String, ?> params) { return request("nba-news", params); }
    public Object oppPtShot(Map<String, ?> params) { return request("nba-opp-pt-shot", params); }
    public Object playByPlay(Map<String, ?> params) { return request("nba-play-by-play", params); }
    public Object playerAwards(Map<String, ?> params) { return request("nba-player-awards", params); }
    public Object playerBioStats(Map<String, ?> params) { return request("nba-player-bio-stats", params); }
    public Object playerCareerStats(Map<String, ?> params) { return request("nba-player-career-stats", params); }
    public Object playerClutch(Map<String, ?> params) { return request("nba-player-clutch", params); }
    public Object playerCompare(Map<String, ?> params) { return request("nba-player-compare", params); }
    public Object playerDashByClutch(Map<String, ?> params) { return request("nba-player-dash-by-clutch", params); }
    public Object playerDashByGameSplits(Map<String, ?> params) { return request("nba-player-dash-by-game-splits", params); }
    public Object playerDashByLastNGames(Map<String, ?> params) { return request("nba-player-dash-by-last-n-games", params); }
    public Object playerDashByOpponent(Map<String, ?> params) { return request("nba-player-dash-by-opponent", params); }
    public Object playerDashPtPass(Map<String, ?> params) { return request("nba-player-dash-pt-pass", params); }
    public Object playerDashPtReb(Map<String, ?> params) { return request("nba-player-dash-pt-reb", params); }
    public Object playerDashPtShots(Map<String, ?> params) { return request("nba-player-dash-pt-shots", params); }
    public Object playerGameLogs(Map<String, ?> params) { return request("nba-player-game-logs", params); }
    public Object playerInfo(Map<String, ?> params) { return request("nba-player-info", params); }
    public Object playerProfileV2(Map<String, ?> params) { return request("nba-player-profile-v2", params); }
    public Object playerPtShot(Map<String, ?> params) { return request("nba-player-pt-shot", params); }
    public Object playerStats(Map<String, ?> params) { return request("nba-player-stats", params); }
    public Object playerStreakFinder(Map<String, ?> params) { return request("nba-player-streak-finder", params); }
    public Object players(Map<String, ?> params) { return request("nba-players", params); }
    public Object playoffPicture(Map<String, ?> params) { return request("nba-playoff-picture", params); }
    public Object playoffSeries(Map<String, ?> params) { return request("nba-playoff-series", params); }
    public Object ptDefend(Map<String, ?> params) { return request("nba-pt-defend", params); }
    public Object ptStats(Map<String, ?> params) { return request("nba-pt-stats", params); }
    public Object scoreboard(Map<String, ?> params) { return request("nba-scoreboard", params); }
    public Object shotChart(Map<String, ?> params) { return request("nba-shot-chart", params); }
    public Object standings(Map<String, ?> params) { return request("nba-standings", params); }
    public Object synergyPlayTypes(Map<String, ?> params) { return request("nba-synergy-play-types", params); }
    public Object teamDashByClutch(Map<String, ?> params) { return request("nba-team-dash-by-clutch", params); }
    public Object teamDashByGameSplits(Map<String, ?> params) { return request("nba-team-dash-by-game-splits", params); }
    public Object teamDashByLastNGames(Map<String, ?> params) { return request("nba-team-dash-by-last-n-games", params); }
    public Object teamDashByOpponent(Map<String, ?> params) { return request("nba-team-dash-by-opponent", params); }
    public Object teamDashPtPass(Map<String, ?> params) { return request("nba-team-dash-pt-pass", params); }
    public Object teamDashPtReb(Map<String, ?> params) { return request("nba-team-dash-pt-reb", params); }
    public Object teamDashPtShots(Map<String, ?> params) { return request("nba-team-dash-pt-shots", params); }
    public Object teamDetails(Map<String, ?> params) { return request("nba-team-details", params); }
    public Object teamGameLogs(Map<String, ?> params) { return request("nba-team-game-logs", params); }
    public Object teamInfoCommon(Map<String, ?> params) { return request("nba-team-info-common", params); }
    public Object teamOnOff(Map<String, ?> params) { return request("nba-team-on-off", params); }
    public Object teamPtShot(Map<String, ?> params) { return request("nba-team-pt-shot", params); }
    public Object teamRoster(Map<String, ?> params) { return request("nba-team-roster", params); }
    public Object teamShotLocations(Map<String, ?> params) { return request("nba-team-shot-locations", params); }
    public Object teamStats(Map<String, ?> params) { return request("nba-team-stats", params); }
    public Object teamStatsLeaders(Map<String, ?> params) { return request("nba-team-stats-leaders", params); }
    public Object teamYears(Map<String, ?> params) { return request("nba-team-years", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
