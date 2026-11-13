"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class NBAClient(CrawloraClient):
    """Synchronous NBA API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-nba-python/0.1.0')
        super().__init__(*args, **kwargs)

    def box_score(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_advanced(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-advanced', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_defensive(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-defensive', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_four_factors(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-four-factors', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_misc(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-misc', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_player_track(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-player-track', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_scoring(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-scoring', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_summary(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-summary', params, response_type=response_type, timeout=timeout, headers=headers)

    def box_score_usage(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-box-score-usage', params, response_type=response_type, timeout=timeout, headers=headers)

    def common_all_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-common-all-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def draft_combine_anthro(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-draft-combine-anthro', params, response_type=response_type, timeout=timeout, headers=headers)

    def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    def franchise_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-franchise-history', params, response_type=response_type, timeout=timeout, headers=headers)

    def game_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-game-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def homepage_leaders(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-homepage-leaders', params, response_type=response_type, timeout=timeout, headers=headers)

    def homepage_v2(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-homepage-v2', params, response_type=response_type, timeout=timeout, headers=headers)

    def hustle_player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-hustle-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def hustle_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-hustle-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def hustle_team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-hustle-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def league_game_log(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-league-game-log', params, response_type=response_type, timeout=timeout, headers=headers)

    def lineup_shot_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-lineup-shot-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    def lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def opp_pt_shot(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-opp-pt-shot', params, response_type=response_type, timeout=timeout, headers=headers)

    def play_by_play(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-play-by-play', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_bio_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-bio-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_career_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-career-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_clutch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-clutch', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_compare(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-compare', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_by_clutch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-by-clutch', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_by_game_splits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-by-game-splits', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_by_last_n_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-by-last-n-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_by_opponent(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-by-opponent', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_pt_pass(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-pt-pass', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_pt_reb(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-pt-reb', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_dash_pt_shots(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-dash-pt-shots', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_game_logs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-game-logs', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_profile_v2(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-profile-v2', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_pt_shot(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-pt-shot', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_streak_finder(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-player-streak-finder', params, response_type=response_type, timeout=timeout, headers=headers)

    def players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def playoff_picture(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-playoff-picture', params, response_type=response_type, timeout=timeout, headers=headers)

    def playoff_series(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-playoff-series', params, response_type=response_type, timeout=timeout, headers=headers)

    def pt_defend(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-pt-defend', params, response_type=response_type, timeout=timeout, headers=headers)

    def pt_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-pt-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def scoreboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-scoreboard', params, response_type=response_type, timeout=timeout, headers=headers)

    def shot_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-shot-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def synergy_play_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-synergy-play-types', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_by_clutch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-by-clutch', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_by_game_splits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-by-game-splits', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_by_last_n_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-by-last-n-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_by_opponent(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-by-opponent', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_pt_pass(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-pt-pass', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_pt_reb(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-pt-reb', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_dash_pt_shots(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-dash-pt-shots', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_details(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-details', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_game_logs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-game-logs', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_info_common(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-info-common', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_on_off(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-on-off', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_pt_shot(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-pt-shot', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_roster(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-roster', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_shot_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-shot-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_stats_leaders(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-stats-leaders', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_years(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('nba-team-years', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncNBAClient(AsyncCrawloraClient):
    """Asynchronous NBA API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-nba-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def box_score(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_advanced(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-advanced', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_defensive(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-defensive', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_four_factors(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-four-factors', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_misc(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-misc', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_player_track(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-player-track', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_scoring(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-scoring', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_summary(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-summary', params, response_type=response_type, timeout=timeout, headers=headers)

    async def box_score_usage(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-box-score-usage', params, response_type=response_type, timeout=timeout, headers=headers)

    async def common_all_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-common-all-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def draft_combine_anthro(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-draft-combine-anthro', params, response_type=response_type, timeout=timeout, headers=headers)

    async def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def franchise_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-franchise-history', params, response_type=response_type, timeout=timeout, headers=headers)

    async def game_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-game-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def homepage_leaders(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-homepage-leaders', params, response_type=response_type, timeout=timeout, headers=headers)

    async def homepage_v2(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-homepage-v2', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hustle_player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-hustle-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hustle_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-hustle-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hustle_team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-hustle-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league_game_log(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-league-game-log', params, response_type=response_type, timeout=timeout, headers=headers)

    async def lineup_shot_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-lineup-shot-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    async def lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def opp_pt_shot(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-opp-pt-shot', params, response_type=response_type, timeout=timeout, headers=headers)

    async def play_by_play(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-play-by-play', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_bio_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-bio-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_career_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-career-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_clutch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-clutch', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_compare(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-compare', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_by_clutch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-by-clutch', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_by_game_splits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-by-game-splits', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_by_last_n_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-by-last-n-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_by_opponent(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-by-opponent', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_pt_pass(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-pt-pass', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_pt_reb(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-pt-reb', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_dash_pt_shots(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-dash-pt-shots', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_game_logs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-game-logs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_profile_v2(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-profile-v2', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_pt_shot(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-pt-shot', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_streak_finder(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-player-streak-finder', params, response_type=response_type, timeout=timeout, headers=headers)

    async def players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playoff_picture(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-playoff-picture', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playoff_series(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-playoff-series', params, response_type=response_type, timeout=timeout, headers=headers)

    async def pt_defend(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-pt-defend', params, response_type=response_type, timeout=timeout, headers=headers)

    async def pt_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-pt-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scoreboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-scoreboard', params, response_type=response_type, timeout=timeout, headers=headers)

    async def shot_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-shot-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    async def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def synergy_play_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-synergy-play-types', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_by_clutch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-by-clutch', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_by_game_splits(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-by-game-splits', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_by_last_n_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-by-last-n-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_by_opponent(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-by-opponent', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_pt_pass(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-pt-pass', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_pt_reb(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-pt-reb', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_dash_pt_shots(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-dash-pt-shots', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_details(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-details', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_game_logs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-game-logs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_info_common(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-info-common', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_on_off(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-on-off', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_pt_shot(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-pt-shot', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_roster(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-roster', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_shot_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-shot-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_stats_leaders(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-stats-leaders', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_years(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('nba-team-years', params, response_type=response_type, timeout=timeout, headers=headers)
