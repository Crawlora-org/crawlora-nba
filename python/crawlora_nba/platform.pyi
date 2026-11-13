from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelNbaTablesResponse = TypedDict('ModelNbaTablesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'tables': NotRequired[list[ModelNbaTable]],
}, total=False)

ModelNbaTable = TypedDict('ModelNbaTable', {
    'headers': NotRequired[list[str]],
    'name': NotRequired[str],
    'rows': NotRequired[list[ModelNbaRow]],
}, total=False)

ModelNbaRow = dict[str, Any]

ModelNbaScoreboardResponse = TypedDict('ModelNbaScoreboardResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game_date': NotRequired[str],
    'games': NotRequired[list[ModelNbaGame]],
    'league_id': NotRequired[str],
    'league_name': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelNbaGame = TypedDict('ModelNbaGame', {
    'away_team': NotRequired[ModelNbaGameSide],
    'game_clock': NotRequired[str],
    'game_code': NotRequired[str],
    'game_et': NotRequired[str],
    'game_id': NotRequired[str],
    'game_status': NotRequired[ModelNbaFlexInt],
    'game_status_text': NotRequired[str],
    'game_time_utc': NotRequired[str],
    'home_team': NotRequired[ModelNbaGameSide],
    'period': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaFlexInt = TypedDict('ModelNbaFlexInt', {
    'value': NotRequired[int],
}, total=False)

ModelNbaGameSide = TypedDict('ModelNbaGameSide', {
    'losses': NotRequired[ModelNbaFlexInt],
    'score': NotRequired[ModelNbaFlexInt],
    'team_city': NotRequired[str],
    'team_id': NotRequired[ModelNbaFlexInt],
    'team_name': NotRequired[str],
    'team_tricode': NotRequired[str],
    'wins': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaPlayByPlayResponse = TypedDict('ModelNbaPlayByPlayResponse', {
    'actions': NotRequired[list[ModelNbaPlayAction]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[str],
    'source_url': NotRequired[str],
    'video_available': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaPlayAction = TypedDict('ModelNbaPlayAction', {
    'action_number': NotRequired[ModelNbaFlexInt],
    'action_type': NotRequired[str],
    'clock': NotRequired[str],
    'description': NotRequired[str],
    'is_field_goal': NotRequired[ModelNbaFlexInt],
    'period': NotRequired[ModelNbaFlexInt],
    'person_id': NotRequired[ModelNbaFlexInt],
    'player_name': NotRequired[str],
    'points_total': NotRequired[ModelNbaFlexInt],
    'score_away': NotRequired[ModelNbaFlexInt],
    'score_home': NotRequired[ModelNbaFlexInt],
    'shot_result': NotRequired[str],
    'shot_value': NotRequired[ModelNbaFlexInt],
    'sub_type': NotRequired[str],
    'team_id': NotRequired[ModelNbaFlexInt],
    'team_tricode': NotRequired[str],
}, total=False)

ModelNbaNewsResponse = TypedDict('ModelNbaNewsResponse', {
    'articles': NotRequired[list[ModelNbaArticle]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelNbaArticle = TypedDict('ModelNbaArticle', {
    'category': NotRequired[ModelNbaArticleCategory],
    'date': NotRequired[str],
    'excerpt': NotRequired[str],
    'id': NotRequired[ModelNbaFlexInt],
    'modified': NotRequired[str],
    'permalink': NotRequired[str],
    'slug': NotRequired[str],
    'status': NotRequired[str],
    'title': NotRequired[str],
    'word_count': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaArticleCategory = TypedDict('ModelNbaArticleCategory', {
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelNbaGamesResponse = TypedDict('ModelNbaGamesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelNbaGame]],
    'source_url': NotRequired[str],
}, total=False)

ModelNbaGameDetailResponse = TypedDict('ModelNbaGameDetailResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[ModelNbaGameDetail],
    'source_url': NotRequired[str],
}, total=False)

ModelNbaGameDetail = TypedDict('ModelNbaGameDetail', {
    'arena': NotRequired[ModelNbaArena],
    'attendance': NotRequired[ModelNbaFlexInt],
    'away_team': NotRequired[ModelNbaDetailTeam],
    'duration': NotRequired[str],
    'game_clock': NotRequired[str],
    'game_code': NotRequired[str],
    'game_et': NotRequired[str],
    'game_id': NotRequired[str],
    'game_label': NotRequired[str],
    'game_status': NotRequired[ModelNbaFlexInt],
    'game_status_text': NotRequired[str],
    'game_sub_label': NotRequired[str],
    'game_time_utc': NotRequired[str],
    'home_team': NotRequired[ModelNbaDetailTeam],
    'if_necessary': NotRequired[bool],
    'is_neutral': NotRequired[bool],
    'officials': NotRequired[list[ModelNbaOfficial]],
    'period': NotRequired[ModelNbaFlexInt],
    'sellout': NotRequired[ModelNbaFlexInt],
    'series_game_number': NotRequired[str],
    'series_text': NotRequired[str],
}, total=False)

ModelNbaOfficial = TypedDict('ModelNbaOfficial', {
    'family_name': NotRequired[str],
    'first_name': NotRequired[str],
    'jersey_num': NotRequired[str],
    'name': NotRequired[str],
    'name_initial': NotRequired[str],
    'person_id': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaDetailTeam = TypedDict('ModelNbaDetailTeam', {
    'periods': NotRequired[list[ModelNbaPeriodScore]],
    'score': NotRequired[ModelNbaFlexInt],
    'team_id': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaPeriodScore = TypedDict('ModelNbaPeriodScore', {
    'period': NotRequired[ModelNbaFlexInt],
    'period_type': NotRequired[str],
    'score': NotRequired[ModelNbaFlexInt],
}, total=False)

ModelNbaArena = TypedDict('ModelNbaArena', {
    'arena_id': NotRequired[ModelNbaFlexInt],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'name': NotRequired[str],
    'state': NotRequired[str],
    'timezone': NotRequired[str],
}, total=False)

ModelNbaEnumsResponse = TypedDict('ModelNbaEnumsResponse', {
    'count': NotRequired[int],
    'data': NotRequired[ModelNbaEnumsData],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelNbaEnumsData = TypedDict('ModelNbaEnumsData', {
    'ahead_behinds': NotRequired[list[str]],
    'blocked': NotRequired[list[str]],
    'clutch_times': NotRequired[list[str]],
    'defense_categories': NotRequired[list[str]],
    'game_date_format': NotRequired[str],
    'league_ids': NotRequired[list[str]],
    'measure_types': NotRequired[list[str]],
    'notes': NotRequired[list[str]],
    'per_modes': NotRequired[list[str]],
    'scopes': NotRequired[list[str]],
    'season_format': NotRequired[str],
    'season_types': NotRequired[list[str]],
    'stat_categories': NotRequired[list[str]],
    'stat_types': NotRequired[list[str]],
    'verified_on': NotRequired[str],
}, total=False)

ModelNbaBoxScoreStatsResponse = TypedDict('ModelNbaBoxScoreStatsResponse', {
    'away_team': NotRequired[ModelNbaRichStatTeam],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[str],
    'home_team': NotRequired[ModelNbaRichStatTeam],
    'source_url': NotRequired[str],
    'stat_group': NotRequired[str],
}, total=False)

ModelNbaRichStatTeam = TypedDict('ModelNbaRichStatTeam', {
    'players': NotRequired[list[ModelNbaPlayerStatLine]],
    'team_id': NotRequired[ModelNbaFlexInt],
    'team_name': NotRequired[str],
    'team_tricode': NotRequired[str],
}, total=False)

ModelNbaPlayerStatLine = TypedDict('ModelNbaPlayerStatLine', {
    'family_name': NotRequired[str],
    'first_name': NotRequired[str],
    'jersey_num': NotRequired[str],
    'name_initial': NotRequired[str],
    'person_id': NotRequired[ModelNbaFlexInt],
    'position': NotRequired[str],
    'statistics': NotRequired[dict[str, Any]],
}, total=False)

ModelNbaBoxScoreResponse = TypedDict('ModelNbaBoxScoreResponse', {
    'away_team': NotRequired[ModelNbaBoxTeam],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[str],
    'home_team': NotRequired[ModelNbaBoxTeam],
    'source_url': NotRequired[str],
}, total=False)

ModelNbaBoxTeam = TypedDict('ModelNbaBoxTeam', {
    'players': NotRequired[list[ModelNbaBoxPlayer]],
    'team_id': NotRequired[ModelNbaFlexInt],
    'team_name': NotRequired[str],
    'team_tricode': NotRequired[str],
}, total=False)

ModelNbaBoxPlayer = TypedDict('ModelNbaBoxPlayer', {
    'assists': NotRequired[ModelNbaFlexInt],
    'family_name': NotRequired[str],
    'field_goals_made': NotRequired[ModelNbaFlexInt],
    'first_name': NotRequired[str],
    'jersey_num': NotRequired[str],
    'minutes': NotRequired[str],
    'name_initial': NotRequired[str],
    'person_id': NotRequired[ModelNbaFlexInt],
    'points': NotRequired[ModelNbaFlexInt],
    'position': NotRequired[str],
    'rebounds': NotRequired[ModelNbaFlexInt],
    'starter': NotRequired[ModelNbaFlexInt],
}, total=False)

NbaBoxScoreResponse = Any
NbaBoxScoreParams = TypedDict('NbaBoxScoreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreAdvancedResponse = Any
NbaBoxScoreAdvancedParams = TypedDict('NbaBoxScoreAdvancedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreDefensiveResponse = Any
NbaBoxScoreDefensiveParams = TypedDict('NbaBoxScoreDefensiveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreFourFactorsResponse = Any
NbaBoxScoreFourFactorsParams = TypedDict('NbaBoxScoreFourFactorsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreMiscResponse = Any
NbaBoxScoreMiscParams = TypedDict('NbaBoxScoreMiscParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScorePlayerTrackResponse = Any
NbaBoxScorePlayerTrackParams = TypedDict('NbaBoxScorePlayerTrackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreScoringResponse = Any
NbaBoxScoreScoringParams = TypedDict('NbaBoxScoreScoringParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreSummaryResponse = Any
NbaBoxScoreSummaryParams = TypedDict('NbaBoxScoreSummaryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreUsageResponse = Any
NbaBoxScoreUsageParams = TypedDict('NbaBoxScoreUsageParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaCommonAllPlayersResponse = Any
NbaCommonAllPlayersParams = TypedDict('NbaCommonAllPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'is_only_current_season': NotRequired[bool],
}, total=False)

NbaDraftCombineAnthroResponse = Any
NbaDraftCombineAnthroParams = TypedDict('NbaDraftCombineAnthroParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'season_year': Required[str],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaEnumsResponse = Any
NbaEnumsParams = TypedDict('NbaEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

NbaFranchiseHistoryResponse = Any
NbaFranchiseHistoryParams = TypedDict('NbaFranchiseHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'team_id': NotRequired[int],
}, total=False)

NbaGameDetailResponse = Any
NbaGameDetailParams = TypedDict('NbaGameDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
}, total=False)

NbaGamesResponse = Any
NbaGamesParams = TypedDict('NbaGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

NbaHomepageLeadersResponse = Any
NbaHomepageLeadersParams = TypedDict('NbaHomepageLeadersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'stat_category': NotRequired[Literal['Points', 'Rebounds']],
    'player_or_team': NotRequired[Literal['Team']],
    'player_scope': NotRequired[str],
    'game_scope': NotRequired[Literal['Season']],
}, total=False)

NbaHomepageV2Response = Any
NbaHomepageV2Params = TypedDict('NbaHomepageV2Params', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'game_scope': NotRequired[Literal['Season']],
    'player_scope': NotRequired[str],
    'player_or_team': NotRequired[Literal['Player']],
    'stat_type': NotRequired[Literal['Traditional']],
}, total=False)

NbaHustlePlayerResponse = Any
NbaHustlePlayerParams = TypedDict('NbaHustlePlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaHustleStatsResponse = Any
NbaHustleStatsParams = TypedDict('NbaHustleStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
}, total=False)

NbaHustleTeamResponse = Any
NbaHustleTeamParams = TypedDict('NbaHustleTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaLeagueGameLogResponse = Any
NbaLeagueGameLogParams = TypedDict('NbaLeagueGameLogParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'direction': NotRequired[Literal['DESC']],
    'player_or_team': NotRequired[Literal['T']],
    'sorter': NotRequired[Literal['DATE']],
}, total=False)

NbaLineupShotChartResponse = Any
NbaLineupShotChartParams = TypedDict('NbaLineupShotChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
    'group_quantity': NotRequired[Literal['5']],
    'period': NotRequired[int],
}, total=False)

NbaLineupsResponse = Any
NbaLineupsParams = TypedDict('NbaLineupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'group_quantity': NotRequired[Literal['5']],
}, total=False)

NbaNewsResponse = Any
NbaNewsParams = TypedDict('NbaNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

NbaOppPtShotResponse = Any
NbaOppPtShotParams = TypedDict('NbaOppPtShotParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayByPlayResponse = Any
NbaPlayByPlayParams = TypedDict('NbaPlayByPlayParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaPlayerAwardsResponse = Any
NbaPlayerAwardsParams = TypedDict('NbaPlayerAwardsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
}, total=False)

NbaPlayerBioStatsResponse = Any
NbaPlayerBioStatsParams = TypedDict('NbaPlayerBioStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerCareerStatsResponse = Any
NbaPlayerCareerStatsParams = TypedDict('NbaPlayerCareerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame']],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerClutchResponse = Any
NbaPlayerClutchParams = TypedDict('NbaPlayerClutchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'clutch_time': NotRequired[Literal['Last 5 Minutes']],
    'ahead_behind': NotRequired[Literal['Ahead or Behind']],
    'point_diff': NotRequired[Literal['5']],
}, total=False)

NbaPlayerCompareResponse = Any
NbaPlayerCompareParams = TypedDict('NbaPlayerCompareParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_ids': Required[list[str]],
    'vs_player_ids': Required[list[str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByClutchResponse = Any
NbaPlayerDashByClutchParams = TypedDict('NbaPlayerDashByClutchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByGameSplitsResponse = Any
NbaPlayerDashByGameSplitsParams = TypedDict('NbaPlayerDashByGameSplitsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByLastNGamesResponse = Any
NbaPlayerDashByLastNGamesParams = TypedDict('NbaPlayerDashByLastNGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByOpponentResponse = Any
NbaPlayerDashByOpponentParams = TypedDict('NbaPlayerDashByOpponentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashPtPassResponse = Any
NbaPlayerDashPtPassParams = TypedDict('NbaPlayerDashPtPassParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtRebResponse = Any
NbaPlayerDashPtRebParams = TypedDict('NbaPlayerDashPtRebParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtShotsResponse = Any
NbaPlayerDashPtShotsParams = TypedDict('NbaPlayerDashPtShotsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerGameLogsResponse = Any
NbaPlayerGameLogsParams = TypedDict('NbaPlayerGameLogsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': Required[int],
}, total=False)

NbaPlayerInfoResponse = Any
NbaPlayerInfoParams = TypedDict('NbaPlayerInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerProfileV2Response = Any
NbaPlayerProfileV2Params = TypedDict('NbaPlayerProfileV2Params', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerPtShotResponse = Any
NbaPlayerPtShotParams = TypedDict('NbaPlayerPtShotParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerStatsResponse = Any
NbaPlayerStatsParams = TypedDict('NbaPlayerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerStreakFinderResponse = Any
NbaPlayerStreakFinderParams = TypedDict('NbaPlayerStreakFinderParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': NotRequired[int],
    'min_games': NotRequired[int],
}, total=False)

NbaPlayersResponse = Any
NbaPlayersParams = TypedDict('NbaPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'team_id': NotRequired[int],
    'active': NotRequired[bool],
}, total=False)

NbaPlayoffPictureResponse = Any
NbaPlayoffPictureParams = TypedDict('NbaPlayoffPictureParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season_id': NotRequired[str],
}, total=False)

NbaPlayoffSeriesResponse = Any
NbaPlayoffSeriesParams = TypedDict('NbaPlayoffSeriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaPtDefendResponse = Any
NbaPtDefendParams = TypedDict('NbaPtDefendParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'defense_category': NotRequired[Literal['Overall', '3 Pointers']],
}, total=False)

NbaPtStatsResponse = Any
NbaPtStatsParams = TypedDict('NbaPtStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'pt_measure_type': NotRequired[Literal['SpeedDistance']],
}, total=False)

NbaScoreboardResponse = Any
NbaScoreboardParams = TypedDict('NbaScoreboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'game_date': NotRequired[str],
    'day_offset': NotRequired[int],
}, total=False)

NbaShotChartResponse = Any
NbaShotChartParams = TypedDict('NbaShotChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': NotRequired[int],
    'team_id': NotRequired[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
}, total=False)

NbaStandingsResponse = Any
NbaStandingsParams = TypedDict('NbaStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
}, total=False)

NbaSynergyPlayTypesResponse = Any
NbaSynergyPlayTypesParams = TypedDict('NbaSynergyPlayTypesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season_year': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'play_type': NotRequired[Literal['Isolation']],
    'per_mode': NotRequired[Literal['PerGame']],
    'player_or_team': NotRequired[Literal['T']],
    'type_grouping': NotRequired[Literal['offensive']],
}, total=False)

NbaTeamDashByClutchResponse = Any
NbaTeamDashByClutchParams = TypedDict('NbaTeamDashByClutchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByGameSplitsResponse = Any
NbaTeamDashByGameSplitsParams = TypedDict('NbaTeamDashByGameSplitsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByLastNGamesResponse = Any
NbaTeamDashByLastNGamesParams = TypedDict('NbaTeamDashByLastNGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByOpponentResponse = Any
NbaTeamDashByOpponentParams = TypedDict('NbaTeamDashByOpponentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashPtPassResponse = Any
NbaTeamDashPtPassParams = TypedDict('NbaTeamDashPtPassParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDashPtRebResponse = Any
NbaTeamDashPtRebParams = TypedDict('NbaTeamDashPtRebParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaTeamDashPtShotsResponse = Any
NbaTeamDashPtShotsParams = TypedDict('NbaTeamDashPtShotsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDetailsResponse = Any
NbaTeamDetailsParams = TypedDict('NbaTeamDetailsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaTeamGameLogsResponse = Any
NbaTeamGameLogsParams = TypedDict('NbaTeamGameLogsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamInfoCommonResponse = Any
NbaTeamInfoCommonParams = TypedDict('NbaTeamInfoCommonParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamOnOffResponse = Any
NbaTeamOnOffParams = TypedDict('NbaTeamOnOffParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'team_id': Required[int],
}, total=False)

NbaTeamPtShotResponse = Any
NbaTeamPtShotParams = TypedDict('NbaTeamPtShotParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamRosterResponse = Any
NbaTeamRosterParams = TypedDict('NbaTeamRosterParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaTeamShotLocationsResponse = Any
NbaTeamShotLocationsParams = TypedDict('NbaTeamShotLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'distance_range': NotRequired[str],
}, total=False)

NbaTeamStatsResponse = Any
NbaTeamStatsParams = TypedDict('NbaTeamStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamStatsLeadersResponse = Any
NbaTeamStatsLeadersParams = TypedDict('NbaTeamStatsLeadersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'stat_category': Required[Literal['PTS', 'REB', 'AST', 'BLK', 'STL', 'TOV']],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'scope': NotRequired[Literal['S']],
}, total=False)

NbaTeamYearsResponse = Any
NbaTeamYearsParams = TypedDict('NbaTeamYearsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': NotRequired[Literal['00']],
}, total=False)

class NbaGroup:
    @overload
    def box_score(self, **params: Unpack[NbaBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    def box_score(self, **params: Unpack[NbaBoxScoreTextResponseParams]) -> str: ...
    @overload
    def box_score(self, **params: Unpack[NbaBoxScoreDefaultParams]) -> NbaBoxScoreResponse: ...
    @overload
    def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedTextResponseParams]) -> str: ...
    @overload
    def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedDefaultParams]) -> NbaBoxScoreAdvancedResponse: ...
    @overload
    def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveTextResponseParams]) -> str: ...
    @overload
    def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveDefaultParams]) -> NbaBoxScoreDefensiveResponse: ...
    @overload
    def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsTextResponseParams]) -> str: ...
    @overload
    def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsDefaultParams]) -> NbaBoxScoreFourFactorsResponse: ...
    @overload
    def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscTextResponseParams]) -> str: ...
    @overload
    def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscDefaultParams]) -> NbaBoxScoreMiscResponse: ...
    @overload
    def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackTextResponseParams]) -> str: ...
    @overload
    def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackDefaultParams]) -> NbaBoxScorePlayerTrackResponse: ...
    @overload
    def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringTextResponseParams]) -> str: ...
    @overload
    def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringDefaultParams]) -> NbaBoxScoreScoringResponse: ...
    @overload
    def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryTextResponseParams]) -> str: ...
    @overload
    def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryDefaultParams]) -> NbaBoxScoreSummaryResponse: ...
    @overload
    def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageTextResponseParams]) -> str: ...
    @overload
    def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageDefaultParams]) -> NbaBoxScoreUsageResponse: ...
    @overload
    def common_all_players(self, **params: Unpack[NbaCommonAllPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def common_all_players(self, **params: Unpack[NbaCommonAllPlayersTextResponseParams]) -> str: ...
    @overload
    def common_all_players(self, **params: Unpack[NbaCommonAllPlayersDefaultParams]) -> NbaCommonAllPlayersResponse: ...
    @overload
    def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroStreamParams]) -> BinaryIO: ...
    @overload
    def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroTextResponseParams]) -> str: ...
    @overload
    def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroDefaultParams]) -> NbaDraftCombineAnthroResponse: ...
    @overload
    def enums(self, **params: Unpack[NbaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[NbaEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[NbaEnumsDefaultParams]) -> NbaEnumsResponse: ...
    @overload
    def franchise_history(self, **params: Unpack[NbaFranchiseHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def franchise_history(self, **params: Unpack[NbaFranchiseHistoryTextResponseParams]) -> str: ...
    @overload
    def franchise_history(self, **params: Unpack[NbaFranchiseHistoryDefaultParams]) -> NbaFranchiseHistoryResponse: ...
    @overload
    def game_detail(self, **params: Unpack[NbaGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    def game_detail(self, **params: Unpack[NbaGameDetailTextResponseParams]) -> str: ...
    @overload
    def game_detail(self, **params: Unpack[NbaGameDetailDefaultParams]) -> NbaGameDetailResponse: ...
    @overload
    def games(self, **params: Unpack[NbaGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[NbaGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[NbaGamesDefaultParams]) -> NbaGamesResponse: ...
    @overload
    def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersStreamParams]) -> BinaryIO: ...
    @overload
    def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersTextResponseParams]) -> str: ...
    @overload
    def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersDefaultParams]) -> NbaHomepageLeadersResponse: ...
    @overload
    def homepage_v2(self, **params: Unpack[NbaHomepageV2StreamParams]) -> BinaryIO: ...
    @overload
    def homepage_v2(self, **params: Unpack[NbaHomepageV2TextResponseParams]) -> str: ...
    @overload
    def homepage_v2(self, **params: Unpack[NbaHomepageV2DefaultParams]) -> NbaHomepageV2Response: ...
    @overload
    def hustle_player(self, **params: Unpack[NbaHustlePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def hustle_player(self, **params: Unpack[NbaHustlePlayerTextResponseParams]) -> str: ...
    @overload
    def hustle_player(self, **params: Unpack[NbaHustlePlayerDefaultParams]) -> NbaHustlePlayerResponse: ...
    @overload
    def hustle_stats(self, **params: Unpack[NbaHustleStatsStreamParams]) -> BinaryIO: ...
    @overload
    def hustle_stats(self, **params: Unpack[NbaHustleStatsTextResponseParams]) -> str: ...
    @overload
    def hustle_stats(self, **params: Unpack[NbaHustleStatsDefaultParams]) -> NbaHustleStatsResponse: ...
    @overload
    def hustle_team(self, **params: Unpack[NbaHustleTeamStreamParams]) -> BinaryIO: ...
    @overload
    def hustle_team(self, **params: Unpack[NbaHustleTeamTextResponseParams]) -> str: ...
    @overload
    def hustle_team(self, **params: Unpack[NbaHustleTeamDefaultParams]) -> NbaHustleTeamResponse: ...
    @overload
    def league_game_log(self, **params: Unpack[NbaLeagueGameLogStreamParams]) -> BinaryIO: ...
    @overload
    def league_game_log(self, **params: Unpack[NbaLeagueGameLogTextResponseParams]) -> str: ...
    @overload
    def league_game_log(self, **params: Unpack[NbaLeagueGameLogDefaultParams]) -> NbaLeagueGameLogResponse: ...
    @overload
    def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartTextResponseParams]) -> str: ...
    @overload
    def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartDefaultParams]) -> NbaLineupShotChartResponse: ...
    @overload
    def lineups(self, **params: Unpack[NbaLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def lineups(self, **params: Unpack[NbaLineupsTextResponseParams]) -> str: ...
    @overload
    def lineups(self, **params: Unpack[NbaLineupsDefaultParams]) -> NbaLineupsResponse: ...
    @overload
    def news(self, **params: Unpack[NbaNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[NbaNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[NbaNewsDefaultParams]) -> NbaNewsResponse: ...
    @overload
    def opp_pt_shot(self, **params: Unpack[NbaOppPtShotStreamParams]) -> BinaryIO: ...
    @overload
    def opp_pt_shot(self, **params: Unpack[NbaOppPtShotTextResponseParams]) -> str: ...
    @overload
    def opp_pt_shot(self, **params: Unpack[NbaOppPtShotDefaultParams]) -> NbaOppPtShotResponse: ...
    @overload
    def play_by_play(self, **params: Unpack[NbaPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    def play_by_play(self, **params: Unpack[NbaPlayByPlayTextResponseParams]) -> str: ...
    @overload
    def play_by_play(self, **params: Unpack[NbaPlayByPlayDefaultParams]) -> NbaPlayByPlayResponse: ...
    @overload
    def player_awards(self, **params: Unpack[NbaPlayerAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def player_awards(self, **params: Unpack[NbaPlayerAwardsTextResponseParams]) -> str: ...
    @overload
    def player_awards(self, **params: Unpack[NbaPlayerAwardsDefaultParams]) -> NbaPlayerAwardsResponse: ...
    @overload
    def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsTextResponseParams]) -> str: ...
    @overload
    def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsDefaultParams]) -> NbaPlayerBioStatsResponse: ...
    @overload
    def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsTextResponseParams]) -> str: ...
    @overload
    def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsDefaultParams]) -> NbaPlayerCareerStatsResponse: ...
    @overload
    def player_clutch(self, **params: Unpack[NbaPlayerClutchStreamParams]) -> BinaryIO: ...
    @overload
    def player_clutch(self, **params: Unpack[NbaPlayerClutchTextResponseParams]) -> str: ...
    @overload
    def player_clutch(self, **params: Unpack[NbaPlayerClutchDefaultParams]) -> NbaPlayerClutchResponse: ...
    @overload
    def player_compare(self, **params: Unpack[NbaPlayerCompareStreamParams]) -> BinaryIO: ...
    @overload
    def player_compare(self, **params: Unpack[NbaPlayerCompareTextResponseParams]) -> str: ...
    @overload
    def player_compare(self, **params: Unpack[NbaPlayerCompareDefaultParams]) -> NbaPlayerCompareResponse: ...
    @overload
    def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchDefaultParams]) -> NbaPlayerDashByClutchResponse: ...
    @overload
    def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsDefaultParams]) -> NbaPlayerDashByGameSplitsResponse: ...
    @overload
    def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesDefaultParams]) -> NbaPlayerDashByLastNGamesResponse: ...
    @overload
    def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentDefaultParams]) -> NbaPlayerDashByOpponentResponse: ...
    @overload
    def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassTextResponseParams]) -> str: ...
    @overload
    def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassDefaultParams]) -> NbaPlayerDashPtPassResponse: ...
    @overload
    def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebTextResponseParams]) -> str: ...
    @overload
    def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebDefaultParams]) -> NbaPlayerDashPtRebResponse: ...
    @overload
    def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsTextResponseParams]) -> str: ...
    @overload
    def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsDefaultParams]) -> NbaPlayerDashPtShotsResponse: ...
    @overload
    def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsTextResponseParams]) -> str: ...
    @overload
    def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsDefaultParams]) -> NbaPlayerGameLogsResponse: ...
    @overload
    def player_info(self, **params: Unpack[NbaPlayerInfoStreamParams]) -> BinaryIO: ...
    @overload
    def player_info(self, **params: Unpack[NbaPlayerInfoTextResponseParams]) -> str: ...
    @overload
    def player_info(self, **params: Unpack[NbaPlayerInfoDefaultParams]) -> NbaPlayerInfoResponse: ...
    @overload
    def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2StreamParams]) -> BinaryIO: ...
    @overload
    def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2TextResponseParams]) -> str: ...
    @overload
    def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2DefaultParams]) -> NbaPlayerProfileV2Response: ...
    @overload
    def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotStreamParams]) -> BinaryIO: ...
    @overload
    def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotTextResponseParams]) -> str: ...
    @overload
    def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotDefaultParams]) -> NbaPlayerPtShotResponse: ...
    @overload
    def player_stats(self, **params: Unpack[NbaPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[NbaPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[NbaPlayerStatsDefaultParams]) -> NbaPlayerStatsResponse: ...
    @overload
    def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderStreamParams]) -> BinaryIO: ...
    @overload
    def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderTextResponseParams]) -> str: ...
    @overload
    def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderDefaultParams]) -> NbaPlayerStreakFinderResponse: ...
    @overload
    def players(self, **params: Unpack[NbaPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def players(self, **params: Unpack[NbaPlayersTextResponseParams]) -> str: ...
    @overload
    def players(self, **params: Unpack[NbaPlayersDefaultParams]) -> NbaPlayersResponse: ...
    @overload
    def playoff_picture(self, **params: Unpack[NbaPlayoffPictureStreamParams]) -> BinaryIO: ...
    @overload
    def playoff_picture(self, **params: Unpack[NbaPlayoffPictureTextResponseParams]) -> str: ...
    @overload
    def playoff_picture(self, **params: Unpack[NbaPlayoffPictureDefaultParams]) -> NbaPlayoffPictureResponse: ...
    @overload
    def playoff_series(self, **params: Unpack[NbaPlayoffSeriesStreamParams]) -> BinaryIO: ...
    @overload
    def playoff_series(self, **params: Unpack[NbaPlayoffSeriesTextResponseParams]) -> str: ...
    @overload
    def playoff_series(self, **params: Unpack[NbaPlayoffSeriesDefaultParams]) -> NbaPlayoffSeriesResponse: ...
    @overload
    def pt_defend(self, **params: Unpack[NbaPtDefendStreamParams]) -> BinaryIO: ...
    @overload
    def pt_defend(self, **params: Unpack[NbaPtDefendTextResponseParams]) -> str: ...
    @overload
    def pt_defend(self, **params: Unpack[NbaPtDefendDefaultParams]) -> NbaPtDefendResponse: ...
    @overload
    def pt_stats(self, **params: Unpack[NbaPtStatsStreamParams]) -> BinaryIO: ...
    @overload
    def pt_stats(self, **params: Unpack[NbaPtStatsTextResponseParams]) -> str: ...
    @overload
    def pt_stats(self, **params: Unpack[NbaPtStatsDefaultParams]) -> NbaPtStatsResponse: ...
    @overload
    def scoreboard(self, **params: Unpack[NbaScoreboardStreamParams]) -> BinaryIO: ...
    @overload
    def scoreboard(self, **params: Unpack[NbaScoreboardTextResponseParams]) -> str: ...
    @overload
    def scoreboard(self, **params: Unpack[NbaScoreboardDefaultParams]) -> NbaScoreboardResponse: ...
    @overload
    def shot_chart(self, **params: Unpack[NbaShotChartStreamParams]) -> BinaryIO: ...
    @overload
    def shot_chart(self, **params: Unpack[NbaShotChartTextResponseParams]) -> str: ...
    @overload
    def shot_chart(self, **params: Unpack[NbaShotChartDefaultParams]) -> NbaShotChartResponse: ...
    @overload
    def standings(self, **params: Unpack[NbaStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[NbaStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[NbaStandingsDefaultParams]) -> NbaStandingsResponse: ...
    @overload
    def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesStreamParams]) -> BinaryIO: ...
    @overload
    def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesTextResponseParams]) -> str: ...
    @overload
    def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesDefaultParams]) -> NbaSynergyPlayTypesResponse: ...
    @overload
    def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchDefaultParams]) -> NbaTeamDashByClutchResponse: ...
    @overload
    def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsDefaultParams]) -> NbaTeamDashByGameSplitsResponse: ...
    @overload
    def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesDefaultParams]) -> NbaTeamDashByLastNGamesResponse: ...
    @overload
    def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentDefaultParams]) -> NbaTeamDashByOpponentResponse: ...
    @overload
    def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassTextResponseParams]) -> str: ...
    @overload
    def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassDefaultParams]) -> NbaTeamDashPtPassResponse: ...
    @overload
    def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebTextResponseParams]) -> str: ...
    @overload
    def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebDefaultParams]) -> NbaTeamDashPtRebResponse: ...
    @overload
    def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsTextResponseParams]) -> str: ...
    @overload
    def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsDefaultParams]) -> NbaTeamDashPtShotsResponse: ...
    @overload
    def team_details(self, **params: Unpack[NbaTeamDetailsStreamParams]) -> BinaryIO: ...
    @overload
    def team_details(self, **params: Unpack[NbaTeamDetailsTextResponseParams]) -> str: ...
    @overload
    def team_details(self, **params: Unpack[NbaTeamDetailsDefaultParams]) -> NbaTeamDetailsResponse: ...
    @overload
    def team_game_logs(self, **params: Unpack[NbaTeamGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    def team_game_logs(self, **params: Unpack[NbaTeamGameLogsTextResponseParams]) -> str: ...
    @overload
    def team_game_logs(self, **params: Unpack[NbaTeamGameLogsDefaultParams]) -> NbaTeamGameLogsResponse: ...
    @overload
    def team_info_common(self, **params: Unpack[NbaTeamInfoCommonStreamParams]) -> BinaryIO: ...
    @overload
    def team_info_common(self, **params: Unpack[NbaTeamInfoCommonTextResponseParams]) -> str: ...
    @overload
    def team_info_common(self, **params: Unpack[NbaTeamInfoCommonDefaultParams]) -> NbaTeamInfoCommonResponse: ...
    @overload
    def team_on_off(self, **params: Unpack[NbaTeamOnOffStreamParams]) -> BinaryIO: ...
    @overload
    def team_on_off(self, **params: Unpack[NbaTeamOnOffTextResponseParams]) -> str: ...
    @overload
    def team_on_off(self, **params: Unpack[NbaTeamOnOffDefaultParams]) -> NbaTeamOnOffResponse: ...
    @overload
    def team_pt_shot(self, **params: Unpack[NbaTeamPtShotStreamParams]) -> BinaryIO: ...
    @overload
    def team_pt_shot(self, **params: Unpack[NbaTeamPtShotTextResponseParams]) -> str: ...
    @overload
    def team_pt_shot(self, **params: Unpack[NbaTeamPtShotDefaultParams]) -> NbaTeamPtShotResponse: ...
    @overload
    def team_roster(self, **params: Unpack[NbaTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    def team_roster(self, **params: Unpack[NbaTeamRosterTextResponseParams]) -> str: ...
    @overload
    def team_roster(self, **params: Unpack[NbaTeamRosterDefaultParams]) -> NbaTeamRosterResponse: ...
    @overload
    def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsTextResponseParams]) -> str: ...
    @overload
    def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsDefaultParams]) -> NbaTeamShotLocationsResponse: ...
    @overload
    def team_stats(self, **params: Unpack[NbaTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    def team_stats(self, **params: Unpack[NbaTeamStatsTextResponseParams]) -> str: ...
    @overload
    def team_stats(self, **params: Unpack[NbaTeamStatsDefaultParams]) -> NbaTeamStatsResponse: ...
    @overload
    def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersStreamParams]) -> BinaryIO: ...
    @overload
    def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersTextResponseParams]) -> str: ...
    @overload
    def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersDefaultParams]) -> NbaTeamStatsLeadersResponse: ...
    @overload
    def team_years(self, **params: Unpack[NbaTeamYearsStreamParams]) -> BinaryIO: ...
    @overload
    def team_years(self, **params: Unpack[NbaTeamYearsTextResponseParams]) -> str: ...
    @overload
    def team_years(self, **params: Unpack[NbaTeamYearsDefaultParams]) -> NbaTeamYearsResponse: ...

OperationId = Literal[
    'nba-box-score',
    'nba-box-score-advanced',
    'nba-box-score-defensive',
    'nba-box-score-four-factors',
    'nba-box-score-misc',
    'nba-box-score-player-track',
    'nba-box-score-scoring',
    'nba-box-score-summary',
    'nba-box-score-usage',
    'nba-common-all-players',
    'nba-draft-combine-anthro',
    'nba-enums',
    'nba-franchise-history',
    'nba-game-detail',
    'nba-games',
    'nba-homepage-leaders',
    'nba-homepage-v2',
    'nba-hustle-player',
    'nba-hustle-stats',
    'nba-hustle-team',
    'nba-league-game-log',
    'nba-lineup-shot-chart',
    'nba-lineups',
    'nba-news',
    'nba-opp-pt-shot',
    'nba-play-by-play',
    'nba-player-awards',
    'nba-player-bio-stats',
    'nba-player-career-stats',
    'nba-player-clutch',
    'nba-player-compare',
    'nba-player-dash-by-clutch',
    'nba-player-dash-by-game-splits',
    'nba-player-dash-by-last-n-games',
    'nba-player-dash-by-opponent',
    'nba-player-dash-pt-pass',
    'nba-player-dash-pt-reb',
    'nba-player-dash-pt-shots',
    'nba-player-game-logs',
    'nba-player-info',
    'nba-player-profile-v2',
    'nba-player-pt-shot',
    'nba-player-stats',
    'nba-player-streak-finder',
    'nba-players',
    'nba-playoff-picture',
    'nba-playoff-series',
    'nba-pt-defend',
    'nba-pt-stats',
    'nba-scoreboard',
    'nba-shot-chart',
    'nba-standings',
    'nba-synergy-play-types',
    'nba-team-dash-by-clutch',
    'nba-team-dash-by-game-splits',
    'nba-team-dash-by-last-n-games',
    'nba-team-dash-by-opponent',
    'nba-team-dash-pt-pass',
    'nba-team-dash-pt-reb',
    'nba-team-dash-pt-shots',
    'nba-team-details',
    'nba-team-game-logs',
    'nba-team-info-common',
    'nba-team-on-off',
    'nba-team-pt-shot',
    'nba-team-roster',
    'nba-team-shot-locations',
    'nba-team-stats',
    'nba-team-stats-leaders',
    'nba-team-years',
]

class CrawloraClient:
    nba: NbaGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score'],
        params: NbaBoxScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-advanced'],
        params: NbaBoxScoreAdvancedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreAdvancedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-defensive'],
        params: NbaBoxScoreDefensiveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreDefensiveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-four-factors'],
        params: NbaBoxScoreFourFactorsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreFourFactorsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-misc'],
        params: NbaBoxScoreMiscParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreMiscResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-player-track'],
        params: NbaBoxScorePlayerTrackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScorePlayerTrackResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-scoring'],
        params: NbaBoxScoreScoringParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreScoringResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-summary'],
        params: NbaBoxScoreSummaryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreSummaryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-box-score-usage'],
        params: NbaBoxScoreUsageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreUsageResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-common-all-players'],
        params: NbaCommonAllPlayersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaCommonAllPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-draft-combine-anthro'],
        params: NbaDraftCombineAnthroParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaDraftCombineAnthroResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-enums'],
        params: NbaEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-franchise-history'],
        params: NbaFranchiseHistoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaFranchiseHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-game-detail'],
        params: NbaGameDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaGameDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-games'],
        params: NbaGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-homepage-leaders'],
        params: NbaHomepageLeadersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHomepageLeadersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-homepage-v2'],
        params: NbaHomepageV2Params = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHomepageV2Response: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-hustle-player'],
        params: NbaHustlePlayerParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHustlePlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-hustle-stats'],
        params: NbaHustleStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHustleStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-hustle-team'],
        params: NbaHustleTeamParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHustleTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-league-game-log'],
        params: NbaLeagueGameLogParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaLeagueGameLogResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-lineup-shot-chart'],
        params: NbaLineupShotChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaLineupShotChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-lineups'],
        params: NbaLineupsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaLineupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-news'],
        params: NbaNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-opp-pt-shot'],
        params: NbaOppPtShotParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaOppPtShotResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-play-by-play'],
        params: NbaPlayByPlayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayByPlayResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-awards'],
        params: NbaPlayerAwardsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerAwardsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-bio-stats'],
        params: NbaPlayerBioStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerBioStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-career-stats'],
        params: NbaPlayerCareerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerCareerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-clutch'],
        params: NbaPlayerClutchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerClutchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-compare'],
        params: NbaPlayerCompareParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerCompareResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-by-clutch'],
        params: NbaPlayerDashByClutchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByClutchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-by-game-splits'],
        params: NbaPlayerDashByGameSplitsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByGameSplitsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-by-last-n-games'],
        params: NbaPlayerDashByLastNGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByLastNGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-by-opponent'],
        params: NbaPlayerDashByOpponentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByOpponentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-pt-pass'],
        params: NbaPlayerDashPtPassParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashPtPassResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-pt-reb'],
        params: NbaPlayerDashPtRebParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashPtRebResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-dash-pt-shots'],
        params: NbaPlayerDashPtShotsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashPtShotsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-game-logs'],
        params: NbaPlayerGameLogsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerGameLogsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-info'],
        params: NbaPlayerInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-profile-v2'],
        params: NbaPlayerProfileV2Params,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerProfileV2Response: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-pt-shot'],
        params: NbaPlayerPtShotParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerPtShotResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-stats'],
        params: NbaPlayerStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-player-streak-finder'],
        params: NbaPlayerStreakFinderParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerStreakFinderResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-players'],
        params: NbaPlayersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-playoff-picture'],
        params: NbaPlayoffPictureParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayoffPictureResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-playoff-series'],
        params: NbaPlayoffSeriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayoffSeriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-pt-defend'],
        params: NbaPtDefendParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPtDefendResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-pt-stats'],
        params: NbaPtStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPtStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-scoreboard'],
        params: NbaScoreboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaScoreboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-shot-chart'],
        params: NbaShotChartParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaShotChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-standings'],
        params: NbaStandingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-synergy-play-types'],
        params: NbaSynergyPlayTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaSynergyPlayTypesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-by-clutch'],
        params: NbaTeamDashByClutchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByClutchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-by-game-splits'],
        params: NbaTeamDashByGameSplitsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByGameSplitsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-by-last-n-games'],
        params: NbaTeamDashByLastNGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByLastNGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-by-opponent'],
        params: NbaTeamDashByOpponentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByOpponentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-pt-pass'],
        params: NbaTeamDashPtPassParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashPtPassResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-pt-reb'],
        params: NbaTeamDashPtRebParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashPtRebResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-dash-pt-shots'],
        params: NbaTeamDashPtShotsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashPtShotsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-details'],
        params: NbaTeamDetailsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDetailsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-game-logs'],
        params: NbaTeamGameLogsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamGameLogsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-info-common'],
        params: NbaTeamInfoCommonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamInfoCommonResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-on-off'],
        params: NbaTeamOnOffParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamOnOffResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-pt-shot'],
        params: NbaTeamPtShotParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamPtShotResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-roster'],
        params: NbaTeamRosterParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamRosterResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-shot-locations'],
        params: NbaTeamShotLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamShotLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-stats'],
        params: NbaTeamStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-stats-leaders'],
        params: NbaTeamStatsLeadersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamStatsLeadersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['nba-team-years'],
        params: NbaTeamYearsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamYearsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score'],
        params: NbaBoxScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-advanced'],
        params: NbaBoxScoreAdvancedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreAdvancedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-defensive'],
        params: NbaBoxScoreDefensiveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreDefensiveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-four-factors'],
        params: NbaBoxScoreFourFactorsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreFourFactorsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-misc'],
        params: NbaBoxScoreMiscParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreMiscResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-player-track'],
        params: NbaBoxScorePlayerTrackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScorePlayerTrackResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-scoring'],
        params: NbaBoxScoreScoringParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreScoringResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-summary'],
        params: NbaBoxScoreSummaryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreSummaryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-box-score-usage'],
        params: NbaBoxScoreUsageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaBoxScoreUsageResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-common-all-players'],
        params: NbaCommonAllPlayersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaCommonAllPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-draft-combine-anthro'],
        params: NbaDraftCombineAnthroParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaDraftCombineAnthroResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-enums'],
        params: NbaEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-franchise-history'],
        params: NbaFranchiseHistoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaFranchiseHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-game-detail'],
        params: NbaGameDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaGameDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-games'],
        params: NbaGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-homepage-leaders'],
        params: NbaHomepageLeadersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHomepageLeadersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-homepage-v2'],
        params: NbaHomepageV2Params = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHomepageV2Response: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-hustle-player'],
        params: NbaHustlePlayerParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHustlePlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-hustle-stats'],
        params: NbaHustleStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHustleStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-hustle-team'],
        params: NbaHustleTeamParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaHustleTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-league-game-log'],
        params: NbaLeagueGameLogParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaLeagueGameLogResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-lineup-shot-chart'],
        params: NbaLineupShotChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaLineupShotChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-lineups'],
        params: NbaLineupsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaLineupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-news'],
        params: NbaNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-opp-pt-shot'],
        params: NbaOppPtShotParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaOppPtShotResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-play-by-play'],
        params: NbaPlayByPlayParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayByPlayResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-awards'],
        params: NbaPlayerAwardsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerAwardsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-bio-stats'],
        params: NbaPlayerBioStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerBioStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-career-stats'],
        params: NbaPlayerCareerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerCareerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-clutch'],
        params: NbaPlayerClutchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerClutchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-compare'],
        params: NbaPlayerCompareParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerCompareResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-by-clutch'],
        params: NbaPlayerDashByClutchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByClutchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-by-game-splits'],
        params: NbaPlayerDashByGameSplitsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByGameSplitsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-by-last-n-games'],
        params: NbaPlayerDashByLastNGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByLastNGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-by-opponent'],
        params: NbaPlayerDashByOpponentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashByOpponentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-pt-pass'],
        params: NbaPlayerDashPtPassParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashPtPassResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-pt-reb'],
        params: NbaPlayerDashPtRebParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashPtRebResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-dash-pt-shots'],
        params: NbaPlayerDashPtShotsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerDashPtShotsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-game-logs'],
        params: NbaPlayerGameLogsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerGameLogsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-info'],
        params: NbaPlayerInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-profile-v2'],
        params: NbaPlayerProfileV2Params,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerProfileV2Response: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-pt-shot'],
        params: NbaPlayerPtShotParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerPtShotResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-stats'],
        params: NbaPlayerStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-player-streak-finder'],
        params: NbaPlayerStreakFinderParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayerStreakFinderResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-players'],
        params: NbaPlayersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-playoff-picture'],
        params: NbaPlayoffPictureParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayoffPictureResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-playoff-series'],
        params: NbaPlayoffSeriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPlayoffSeriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-pt-defend'],
        params: NbaPtDefendParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPtDefendResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-pt-stats'],
        params: NbaPtStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaPtStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-scoreboard'],
        params: NbaScoreboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaScoreboardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-shot-chart'],
        params: NbaShotChartParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaShotChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-standings'],
        params: NbaStandingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-synergy-play-types'],
        params: NbaSynergyPlayTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaSynergyPlayTypesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-by-clutch'],
        params: NbaTeamDashByClutchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByClutchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-by-game-splits'],
        params: NbaTeamDashByGameSplitsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByGameSplitsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-by-last-n-games'],
        params: NbaTeamDashByLastNGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByLastNGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-by-opponent'],
        params: NbaTeamDashByOpponentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashByOpponentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-pt-pass'],
        params: NbaTeamDashPtPassParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashPtPassResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-pt-reb'],
        params: NbaTeamDashPtRebParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashPtRebResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-dash-pt-shots'],
        params: NbaTeamDashPtShotsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDashPtShotsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-details'],
        params: NbaTeamDetailsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamDetailsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-game-logs'],
        params: NbaTeamGameLogsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamGameLogsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-info-common'],
        params: NbaTeamInfoCommonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamInfoCommonResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-on-off'],
        params: NbaTeamOnOffParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamOnOffResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-pt-shot'],
        params: NbaTeamPtShotParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamPtShotResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-roster'],
        params: NbaTeamRosterParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamRosterResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-shot-locations'],
        params: NbaTeamShotLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamShotLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-stats'],
        params: NbaTeamStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-stats-leaders'],
        params: NbaTeamStatsLeadersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamStatsLeadersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['nba-team-years'],
        params: NbaTeamYearsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> NbaTeamYearsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class NBAClient(CrawloraClient):
    def __enter__(self) -> NBAClient: ...
    @overload
    def box_score(self, **params: Unpack[NbaBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    def box_score(self, **params: Unpack[NbaBoxScoreTextResponseParams]) -> str: ...
    @overload
    def box_score(self, **params: Unpack[NbaBoxScoreDefaultParams]) -> NbaBoxScoreResponse: ...
    @overload
    def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedTextResponseParams]) -> str: ...
    @overload
    def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedDefaultParams]) -> NbaBoxScoreAdvancedResponse: ...
    @overload
    def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveTextResponseParams]) -> str: ...
    @overload
    def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveDefaultParams]) -> NbaBoxScoreDefensiveResponse: ...
    @overload
    def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsTextResponseParams]) -> str: ...
    @overload
    def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsDefaultParams]) -> NbaBoxScoreFourFactorsResponse: ...
    @overload
    def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscTextResponseParams]) -> str: ...
    @overload
    def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscDefaultParams]) -> NbaBoxScoreMiscResponse: ...
    @overload
    def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackTextResponseParams]) -> str: ...
    @overload
    def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackDefaultParams]) -> NbaBoxScorePlayerTrackResponse: ...
    @overload
    def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringTextResponseParams]) -> str: ...
    @overload
    def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringDefaultParams]) -> NbaBoxScoreScoringResponse: ...
    @overload
    def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryTextResponseParams]) -> str: ...
    @overload
    def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryDefaultParams]) -> NbaBoxScoreSummaryResponse: ...
    @overload
    def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageStreamParams]) -> BinaryIO: ...
    @overload
    def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageTextResponseParams]) -> str: ...
    @overload
    def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageDefaultParams]) -> NbaBoxScoreUsageResponse: ...
    @overload
    def common_all_players(self, **params: Unpack[NbaCommonAllPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def common_all_players(self, **params: Unpack[NbaCommonAllPlayersTextResponseParams]) -> str: ...
    @overload
    def common_all_players(self, **params: Unpack[NbaCommonAllPlayersDefaultParams]) -> NbaCommonAllPlayersResponse: ...
    @overload
    def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroStreamParams]) -> BinaryIO: ...
    @overload
    def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroTextResponseParams]) -> str: ...
    @overload
    def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroDefaultParams]) -> NbaDraftCombineAnthroResponse: ...
    @overload
    def enums(self, **params: Unpack[NbaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[NbaEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[NbaEnumsDefaultParams]) -> NbaEnumsResponse: ...
    @overload
    def franchise_history(self, **params: Unpack[NbaFranchiseHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def franchise_history(self, **params: Unpack[NbaFranchiseHistoryTextResponseParams]) -> str: ...
    @overload
    def franchise_history(self, **params: Unpack[NbaFranchiseHistoryDefaultParams]) -> NbaFranchiseHistoryResponse: ...
    @overload
    def game_detail(self, **params: Unpack[NbaGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    def game_detail(self, **params: Unpack[NbaGameDetailTextResponseParams]) -> str: ...
    @overload
    def game_detail(self, **params: Unpack[NbaGameDetailDefaultParams]) -> NbaGameDetailResponse: ...
    @overload
    def games(self, **params: Unpack[NbaGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[NbaGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[NbaGamesDefaultParams]) -> NbaGamesResponse: ...
    @overload
    def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersStreamParams]) -> BinaryIO: ...
    @overload
    def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersTextResponseParams]) -> str: ...
    @overload
    def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersDefaultParams]) -> NbaHomepageLeadersResponse: ...
    @overload
    def homepage_v2(self, **params: Unpack[NbaHomepageV2StreamParams]) -> BinaryIO: ...
    @overload
    def homepage_v2(self, **params: Unpack[NbaHomepageV2TextResponseParams]) -> str: ...
    @overload
    def homepage_v2(self, **params: Unpack[NbaHomepageV2DefaultParams]) -> NbaHomepageV2Response: ...
    @overload
    def hustle_player(self, **params: Unpack[NbaHustlePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def hustle_player(self, **params: Unpack[NbaHustlePlayerTextResponseParams]) -> str: ...
    @overload
    def hustle_player(self, **params: Unpack[NbaHustlePlayerDefaultParams]) -> NbaHustlePlayerResponse: ...
    @overload
    def hustle_stats(self, **params: Unpack[NbaHustleStatsStreamParams]) -> BinaryIO: ...
    @overload
    def hustle_stats(self, **params: Unpack[NbaHustleStatsTextResponseParams]) -> str: ...
    @overload
    def hustle_stats(self, **params: Unpack[NbaHustleStatsDefaultParams]) -> NbaHustleStatsResponse: ...
    @overload
    def hustle_team(self, **params: Unpack[NbaHustleTeamStreamParams]) -> BinaryIO: ...
    @overload
    def hustle_team(self, **params: Unpack[NbaHustleTeamTextResponseParams]) -> str: ...
    @overload
    def hustle_team(self, **params: Unpack[NbaHustleTeamDefaultParams]) -> NbaHustleTeamResponse: ...
    @overload
    def league_game_log(self, **params: Unpack[NbaLeagueGameLogStreamParams]) -> BinaryIO: ...
    @overload
    def league_game_log(self, **params: Unpack[NbaLeagueGameLogTextResponseParams]) -> str: ...
    @overload
    def league_game_log(self, **params: Unpack[NbaLeagueGameLogDefaultParams]) -> NbaLeagueGameLogResponse: ...
    @overload
    def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartTextResponseParams]) -> str: ...
    @overload
    def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartDefaultParams]) -> NbaLineupShotChartResponse: ...
    @overload
    def lineups(self, **params: Unpack[NbaLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def lineups(self, **params: Unpack[NbaLineupsTextResponseParams]) -> str: ...
    @overload
    def lineups(self, **params: Unpack[NbaLineupsDefaultParams]) -> NbaLineupsResponse: ...
    @overload
    def news(self, **params: Unpack[NbaNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[NbaNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[NbaNewsDefaultParams]) -> NbaNewsResponse: ...
    @overload
    def opp_pt_shot(self, **params: Unpack[NbaOppPtShotStreamParams]) -> BinaryIO: ...
    @overload
    def opp_pt_shot(self, **params: Unpack[NbaOppPtShotTextResponseParams]) -> str: ...
    @overload
    def opp_pt_shot(self, **params: Unpack[NbaOppPtShotDefaultParams]) -> NbaOppPtShotResponse: ...
    @overload
    def play_by_play(self, **params: Unpack[NbaPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    def play_by_play(self, **params: Unpack[NbaPlayByPlayTextResponseParams]) -> str: ...
    @overload
    def play_by_play(self, **params: Unpack[NbaPlayByPlayDefaultParams]) -> NbaPlayByPlayResponse: ...
    @overload
    def player_awards(self, **params: Unpack[NbaPlayerAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def player_awards(self, **params: Unpack[NbaPlayerAwardsTextResponseParams]) -> str: ...
    @overload
    def player_awards(self, **params: Unpack[NbaPlayerAwardsDefaultParams]) -> NbaPlayerAwardsResponse: ...
    @overload
    def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsTextResponseParams]) -> str: ...
    @overload
    def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsDefaultParams]) -> NbaPlayerBioStatsResponse: ...
    @overload
    def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsTextResponseParams]) -> str: ...
    @overload
    def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsDefaultParams]) -> NbaPlayerCareerStatsResponse: ...
    @overload
    def player_clutch(self, **params: Unpack[NbaPlayerClutchStreamParams]) -> BinaryIO: ...
    @overload
    def player_clutch(self, **params: Unpack[NbaPlayerClutchTextResponseParams]) -> str: ...
    @overload
    def player_clutch(self, **params: Unpack[NbaPlayerClutchDefaultParams]) -> NbaPlayerClutchResponse: ...
    @overload
    def player_compare(self, **params: Unpack[NbaPlayerCompareStreamParams]) -> BinaryIO: ...
    @overload
    def player_compare(self, **params: Unpack[NbaPlayerCompareTextResponseParams]) -> str: ...
    @overload
    def player_compare(self, **params: Unpack[NbaPlayerCompareDefaultParams]) -> NbaPlayerCompareResponse: ...
    @overload
    def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchDefaultParams]) -> NbaPlayerDashByClutchResponse: ...
    @overload
    def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsDefaultParams]) -> NbaPlayerDashByGameSplitsResponse: ...
    @overload
    def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesDefaultParams]) -> NbaPlayerDashByLastNGamesResponse: ...
    @overload
    def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentTextResponseParams]) -> str: ...
    @overload
    def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentDefaultParams]) -> NbaPlayerDashByOpponentResponse: ...
    @overload
    def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassTextResponseParams]) -> str: ...
    @overload
    def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassDefaultParams]) -> NbaPlayerDashPtPassResponse: ...
    @overload
    def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebTextResponseParams]) -> str: ...
    @overload
    def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebDefaultParams]) -> NbaPlayerDashPtRebResponse: ...
    @overload
    def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsTextResponseParams]) -> str: ...
    @overload
    def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsDefaultParams]) -> NbaPlayerDashPtShotsResponse: ...
    @overload
    def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsTextResponseParams]) -> str: ...
    @overload
    def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsDefaultParams]) -> NbaPlayerGameLogsResponse: ...
    @overload
    def player_info(self, **params: Unpack[NbaPlayerInfoStreamParams]) -> BinaryIO: ...
    @overload
    def player_info(self, **params: Unpack[NbaPlayerInfoTextResponseParams]) -> str: ...
    @overload
    def player_info(self, **params: Unpack[NbaPlayerInfoDefaultParams]) -> NbaPlayerInfoResponse: ...
    @overload
    def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2StreamParams]) -> BinaryIO: ...
    @overload
    def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2TextResponseParams]) -> str: ...
    @overload
    def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2DefaultParams]) -> NbaPlayerProfileV2Response: ...
    @overload
    def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotStreamParams]) -> BinaryIO: ...
    @overload
    def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotTextResponseParams]) -> str: ...
    @overload
    def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotDefaultParams]) -> NbaPlayerPtShotResponse: ...
    @overload
    def player_stats(self, **params: Unpack[NbaPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[NbaPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[NbaPlayerStatsDefaultParams]) -> NbaPlayerStatsResponse: ...
    @overload
    def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderStreamParams]) -> BinaryIO: ...
    @overload
    def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderTextResponseParams]) -> str: ...
    @overload
    def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderDefaultParams]) -> NbaPlayerStreakFinderResponse: ...
    @overload
    def players(self, **params: Unpack[NbaPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def players(self, **params: Unpack[NbaPlayersTextResponseParams]) -> str: ...
    @overload
    def players(self, **params: Unpack[NbaPlayersDefaultParams]) -> NbaPlayersResponse: ...
    @overload
    def playoff_picture(self, **params: Unpack[NbaPlayoffPictureStreamParams]) -> BinaryIO: ...
    @overload
    def playoff_picture(self, **params: Unpack[NbaPlayoffPictureTextResponseParams]) -> str: ...
    @overload
    def playoff_picture(self, **params: Unpack[NbaPlayoffPictureDefaultParams]) -> NbaPlayoffPictureResponse: ...
    @overload
    def playoff_series(self, **params: Unpack[NbaPlayoffSeriesStreamParams]) -> BinaryIO: ...
    @overload
    def playoff_series(self, **params: Unpack[NbaPlayoffSeriesTextResponseParams]) -> str: ...
    @overload
    def playoff_series(self, **params: Unpack[NbaPlayoffSeriesDefaultParams]) -> NbaPlayoffSeriesResponse: ...
    @overload
    def pt_defend(self, **params: Unpack[NbaPtDefendStreamParams]) -> BinaryIO: ...
    @overload
    def pt_defend(self, **params: Unpack[NbaPtDefendTextResponseParams]) -> str: ...
    @overload
    def pt_defend(self, **params: Unpack[NbaPtDefendDefaultParams]) -> NbaPtDefendResponse: ...
    @overload
    def pt_stats(self, **params: Unpack[NbaPtStatsStreamParams]) -> BinaryIO: ...
    @overload
    def pt_stats(self, **params: Unpack[NbaPtStatsTextResponseParams]) -> str: ...
    @overload
    def pt_stats(self, **params: Unpack[NbaPtStatsDefaultParams]) -> NbaPtStatsResponse: ...
    @overload
    def scoreboard(self, **params: Unpack[NbaScoreboardStreamParams]) -> BinaryIO: ...
    @overload
    def scoreboard(self, **params: Unpack[NbaScoreboardTextResponseParams]) -> str: ...
    @overload
    def scoreboard(self, **params: Unpack[NbaScoreboardDefaultParams]) -> NbaScoreboardResponse: ...
    @overload
    def shot_chart(self, **params: Unpack[NbaShotChartStreamParams]) -> BinaryIO: ...
    @overload
    def shot_chart(self, **params: Unpack[NbaShotChartTextResponseParams]) -> str: ...
    @overload
    def shot_chart(self, **params: Unpack[NbaShotChartDefaultParams]) -> NbaShotChartResponse: ...
    @overload
    def standings(self, **params: Unpack[NbaStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[NbaStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[NbaStandingsDefaultParams]) -> NbaStandingsResponse: ...
    @overload
    def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesStreamParams]) -> BinaryIO: ...
    @overload
    def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesTextResponseParams]) -> str: ...
    @overload
    def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesDefaultParams]) -> NbaSynergyPlayTypesResponse: ...
    @overload
    def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchDefaultParams]) -> NbaTeamDashByClutchResponse: ...
    @overload
    def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsDefaultParams]) -> NbaTeamDashByGameSplitsResponse: ...
    @overload
    def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesDefaultParams]) -> NbaTeamDashByLastNGamesResponse: ...
    @overload
    def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentTextResponseParams]) -> str: ...
    @overload
    def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentDefaultParams]) -> NbaTeamDashByOpponentResponse: ...
    @overload
    def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassTextResponseParams]) -> str: ...
    @overload
    def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassDefaultParams]) -> NbaTeamDashPtPassResponse: ...
    @overload
    def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebTextResponseParams]) -> str: ...
    @overload
    def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebDefaultParams]) -> NbaTeamDashPtRebResponse: ...
    @overload
    def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsTextResponseParams]) -> str: ...
    @overload
    def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsDefaultParams]) -> NbaTeamDashPtShotsResponse: ...
    @overload
    def team_details(self, **params: Unpack[NbaTeamDetailsStreamParams]) -> BinaryIO: ...
    @overload
    def team_details(self, **params: Unpack[NbaTeamDetailsTextResponseParams]) -> str: ...
    @overload
    def team_details(self, **params: Unpack[NbaTeamDetailsDefaultParams]) -> NbaTeamDetailsResponse: ...
    @overload
    def team_game_logs(self, **params: Unpack[NbaTeamGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    def team_game_logs(self, **params: Unpack[NbaTeamGameLogsTextResponseParams]) -> str: ...
    @overload
    def team_game_logs(self, **params: Unpack[NbaTeamGameLogsDefaultParams]) -> NbaTeamGameLogsResponse: ...
    @overload
    def team_info_common(self, **params: Unpack[NbaTeamInfoCommonStreamParams]) -> BinaryIO: ...
    @overload
    def team_info_common(self, **params: Unpack[NbaTeamInfoCommonTextResponseParams]) -> str: ...
    @overload
    def team_info_common(self, **params: Unpack[NbaTeamInfoCommonDefaultParams]) -> NbaTeamInfoCommonResponse: ...
    @overload
    def team_on_off(self, **params: Unpack[NbaTeamOnOffStreamParams]) -> BinaryIO: ...
    @overload
    def team_on_off(self, **params: Unpack[NbaTeamOnOffTextResponseParams]) -> str: ...
    @overload
    def team_on_off(self, **params: Unpack[NbaTeamOnOffDefaultParams]) -> NbaTeamOnOffResponse: ...
    @overload
    def team_pt_shot(self, **params: Unpack[NbaTeamPtShotStreamParams]) -> BinaryIO: ...
    @overload
    def team_pt_shot(self, **params: Unpack[NbaTeamPtShotTextResponseParams]) -> str: ...
    @overload
    def team_pt_shot(self, **params: Unpack[NbaTeamPtShotDefaultParams]) -> NbaTeamPtShotResponse: ...
    @overload
    def team_roster(self, **params: Unpack[NbaTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    def team_roster(self, **params: Unpack[NbaTeamRosterTextResponseParams]) -> str: ...
    @overload
    def team_roster(self, **params: Unpack[NbaTeamRosterDefaultParams]) -> NbaTeamRosterResponse: ...
    @overload
    def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsTextResponseParams]) -> str: ...
    @overload
    def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsDefaultParams]) -> NbaTeamShotLocationsResponse: ...
    @overload
    def team_stats(self, **params: Unpack[NbaTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    def team_stats(self, **params: Unpack[NbaTeamStatsTextResponseParams]) -> str: ...
    @overload
    def team_stats(self, **params: Unpack[NbaTeamStatsDefaultParams]) -> NbaTeamStatsResponse: ...
    @overload
    def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersStreamParams]) -> BinaryIO: ...
    @overload
    def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersTextResponseParams]) -> str: ...
    @overload
    def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersDefaultParams]) -> NbaTeamStatsLeadersResponse: ...
    @overload
    def team_years(self, **params: Unpack[NbaTeamYearsStreamParams]) -> BinaryIO: ...
    @overload
    def team_years(self, **params: Unpack[NbaTeamYearsTextResponseParams]) -> str: ...
    @overload
    def team_years(self, **params: Unpack[NbaTeamYearsDefaultParams]) -> NbaTeamYearsResponse: ...

class AsyncNBAClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncNBAClient: ...
    nba: _AsyncNbaGroup
    @overload
    async def box_score(self, **params: Unpack[NbaBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score(self, **params: Unpack[NbaBoxScoreTextResponseParams]) -> str: ...
    @overload
    async def box_score(self, **params: Unpack[NbaBoxScoreDefaultParams]) -> NbaBoxScoreResponse: ...
    @overload
    async def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedTextResponseParams]) -> str: ...
    @overload
    async def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedDefaultParams]) -> NbaBoxScoreAdvancedResponse: ...
    @overload
    async def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveTextResponseParams]) -> str: ...
    @overload
    async def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveDefaultParams]) -> NbaBoxScoreDefensiveResponse: ...
    @overload
    async def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsTextResponseParams]) -> str: ...
    @overload
    async def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsDefaultParams]) -> NbaBoxScoreFourFactorsResponse: ...
    @overload
    async def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscTextResponseParams]) -> str: ...
    @overload
    async def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscDefaultParams]) -> NbaBoxScoreMiscResponse: ...
    @overload
    async def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackTextResponseParams]) -> str: ...
    @overload
    async def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackDefaultParams]) -> NbaBoxScorePlayerTrackResponse: ...
    @overload
    async def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringTextResponseParams]) -> str: ...
    @overload
    async def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringDefaultParams]) -> NbaBoxScoreScoringResponse: ...
    @overload
    async def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryTextResponseParams]) -> str: ...
    @overload
    async def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryDefaultParams]) -> NbaBoxScoreSummaryResponse: ...
    @overload
    async def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageTextResponseParams]) -> str: ...
    @overload
    async def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageDefaultParams]) -> NbaBoxScoreUsageResponse: ...
    @overload
    async def common_all_players(self, **params: Unpack[NbaCommonAllPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def common_all_players(self, **params: Unpack[NbaCommonAllPlayersTextResponseParams]) -> str: ...
    @overload
    async def common_all_players(self, **params: Unpack[NbaCommonAllPlayersDefaultParams]) -> NbaCommonAllPlayersResponse: ...
    @overload
    async def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroStreamParams]) -> BinaryIO: ...
    @overload
    async def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroTextResponseParams]) -> str: ...
    @overload
    async def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroDefaultParams]) -> NbaDraftCombineAnthroResponse: ...
    @overload
    async def enums(self, **params: Unpack[NbaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[NbaEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[NbaEnumsDefaultParams]) -> NbaEnumsResponse: ...
    @overload
    async def franchise_history(self, **params: Unpack[NbaFranchiseHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def franchise_history(self, **params: Unpack[NbaFranchiseHistoryTextResponseParams]) -> str: ...
    @overload
    async def franchise_history(self, **params: Unpack[NbaFranchiseHistoryDefaultParams]) -> NbaFranchiseHistoryResponse: ...
    @overload
    async def game_detail(self, **params: Unpack[NbaGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def game_detail(self, **params: Unpack[NbaGameDetailTextResponseParams]) -> str: ...
    @overload
    async def game_detail(self, **params: Unpack[NbaGameDetailDefaultParams]) -> NbaGameDetailResponse: ...
    @overload
    async def games(self, **params: Unpack[NbaGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[NbaGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[NbaGamesDefaultParams]) -> NbaGamesResponse: ...
    @overload
    async def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersStreamParams]) -> BinaryIO: ...
    @overload
    async def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersTextResponseParams]) -> str: ...
    @overload
    async def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersDefaultParams]) -> NbaHomepageLeadersResponse: ...
    @overload
    async def homepage_v2(self, **params: Unpack[NbaHomepageV2StreamParams]) -> BinaryIO: ...
    @overload
    async def homepage_v2(self, **params: Unpack[NbaHomepageV2TextResponseParams]) -> str: ...
    @overload
    async def homepage_v2(self, **params: Unpack[NbaHomepageV2DefaultParams]) -> NbaHomepageV2Response: ...
    @overload
    async def hustle_player(self, **params: Unpack[NbaHustlePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def hustle_player(self, **params: Unpack[NbaHustlePlayerTextResponseParams]) -> str: ...
    @overload
    async def hustle_player(self, **params: Unpack[NbaHustlePlayerDefaultParams]) -> NbaHustlePlayerResponse: ...
    @overload
    async def hustle_stats(self, **params: Unpack[NbaHustleStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def hustle_stats(self, **params: Unpack[NbaHustleStatsTextResponseParams]) -> str: ...
    @overload
    async def hustle_stats(self, **params: Unpack[NbaHustleStatsDefaultParams]) -> NbaHustleStatsResponse: ...
    @overload
    async def hustle_team(self, **params: Unpack[NbaHustleTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def hustle_team(self, **params: Unpack[NbaHustleTeamTextResponseParams]) -> str: ...
    @overload
    async def hustle_team(self, **params: Unpack[NbaHustleTeamDefaultParams]) -> NbaHustleTeamResponse: ...
    @overload
    async def league_game_log(self, **params: Unpack[NbaLeagueGameLogStreamParams]) -> BinaryIO: ...
    @overload
    async def league_game_log(self, **params: Unpack[NbaLeagueGameLogTextResponseParams]) -> str: ...
    @overload
    async def league_game_log(self, **params: Unpack[NbaLeagueGameLogDefaultParams]) -> NbaLeagueGameLogResponse: ...
    @overload
    async def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartTextResponseParams]) -> str: ...
    @overload
    async def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartDefaultParams]) -> NbaLineupShotChartResponse: ...
    @overload
    async def lineups(self, **params: Unpack[NbaLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def lineups(self, **params: Unpack[NbaLineupsTextResponseParams]) -> str: ...
    @overload
    async def lineups(self, **params: Unpack[NbaLineupsDefaultParams]) -> NbaLineupsResponse: ...
    @overload
    async def news(self, **params: Unpack[NbaNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[NbaNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[NbaNewsDefaultParams]) -> NbaNewsResponse: ...
    @overload
    async def opp_pt_shot(self, **params: Unpack[NbaOppPtShotStreamParams]) -> BinaryIO: ...
    @overload
    async def opp_pt_shot(self, **params: Unpack[NbaOppPtShotTextResponseParams]) -> str: ...
    @overload
    async def opp_pt_shot(self, **params: Unpack[NbaOppPtShotDefaultParams]) -> NbaOppPtShotResponse: ...
    @overload
    async def play_by_play(self, **params: Unpack[NbaPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    async def play_by_play(self, **params: Unpack[NbaPlayByPlayTextResponseParams]) -> str: ...
    @overload
    async def play_by_play(self, **params: Unpack[NbaPlayByPlayDefaultParams]) -> NbaPlayByPlayResponse: ...
    @overload
    async def player_awards(self, **params: Unpack[NbaPlayerAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_awards(self, **params: Unpack[NbaPlayerAwardsTextResponseParams]) -> str: ...
    @overload
    async def player_awards(self, **params: Unpack[NbaPlayerAwardsDefaultParams]) -> NbaPlayerAwardsResponse: ...
    @overload
    async def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsTextResponseParams]) -> str: ...
    @overload
    async def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsDefaultParams]) -> NbaPlayerBioStatsResponse: ...
    @overload
    async def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsDefaultParams]) -> NbaPlayerCareerStatsResponse: ...
    @overload
    async def player_clutch(self, **params: Unpack[NbaPlayerClutchStreamParams]) -> BinaryIO: ...
    @overload
    async def player_clutch(self, **params: Unpack[NbaPlayerClutchTextResponseParams]) -> str: ...
    @overload
    async def player_clutch(self, **params: Unpack[NbaPlayerClutchDefaultParams]) -> NbaPlayerClutchResponse: ...
    @overload
    async def player_compare(self, **params: Unpack[NbaPlayerCompareStreamParams]) -> BinaryIO: ...
    @overload
    async def player_compare(self, **params: Unpack[NbaPlayerCompareTextResponseParams]) -> str: ...
    @overload
    async def player_compare(self, **params: Unpack[NbaPlayerCompareDefaultParams]) -> NbaPlayerCompareResponse: ...
    @overload
    async def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchDefaultParams]) -> NbaPlayerDashByClutchResponse: ...
    @overload
    async def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsDefaultParams]) -> NbaPlayerDashByGameSplitsResponse: ...
    @overload
    async def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesDefaultParams]) -> NbaPlayerDashByLastNGamesResponse: ...
    @overload
    async def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentDefaultParams]) -> NbaPlayerDashByOpponentResponse: ...
    @overload
    async def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassTextResponseParams]) -> str: ...
    @overload
    async def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassDefaultParams]) -> NbaPlayerDashPtPassResponse: ...
    @overload
    async def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebTextResponseParams]) -> str: ...
    @overload
    async def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebDefaultParams]) -> NbaPlayerDashPtRebResponse: ...
    @overload
    async def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsTextResponseParams]) -> str: ...
    @overload
    async def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsDefaultParams]) -> NbaPlayerDashPtShotsResponse: ...
    @overload
    async def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsTextResponseParams]) -> str: ...
    @overload
    async def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsDefaultParams]) -> NbaPlayerGameLogsResponse: ...
    @overload
    async def player_info(self, **params: Unpack[NbaPlayerInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def player_info(self, **params: Unpack[NbaPlayerInfoTextResponseParams]) -> str: ...
    @overload
    async def player_info(self, **params: Unpack[NbaPlayerInfoDefaultParams]) -> NbaPlayerInfoResponse: ...
    @overload
    async def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2StreamParams]) -> BinaryIO: ...
    @overload
    async def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2TextResponseParams]) -> str: ...
    @overload
    async def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2DefaultParams]) -> NbaPlayerProfileV2Response: ...
    @overload
    async def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotStreamParams]) -> BinaryIO: ...
    @overload
    async def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotTextResponseParams]) -> str: ...
    @overload
    async def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotDefaultParams]) -> NbaPlayerPtShotResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[NbaPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[NbaPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[NbaPlayerStatsDefaultParams]) -> NbaPlayerStatsResponse: ...
    @overload
    async def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderStreamParams]) -> BinaryIO: ...
    @overload
    async def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderTextResponseParams]) -> str: ...
    @overload
    async def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderDefaultParams]) -> NbaPlayerStreakFinderResponse: ...
    @overload
    async def players(self, **params: Unpack[NbaPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def players(self, **params: Unpack[NbaPlayersTextResponseParams]) -> str: ...
    @overload
    async def players(self, **params: Unpack[NbaPlayersDefaultParams]) -> NbaPlayersResponse: ...
    @overload
    async def playoff_picture(self, **params: Unpack[NbaPlayoffPictureStreamParams]) -> BinaryIO: ...
    @overload
    async def playoff_picture(self, **params: Unpack[NbaPlayoffPictureTextResponseParams]) -> str: ...
    @overload
    async def playoff_picture(self, **params: Unpack[NbaPlayoffPictureDefaultParams]) -> NbaPlayoffPictureResponse: ...
    @overload
    async def playoff_series(self, **params: Unpack[NbaPlayoffSeriesStreamParams]) -> BinaryIO: ...
    @overload
    async def playoff_series(self, **params: Unpack[NbaPlayoffSeriesTextResponseParams]) -> str: ...
    @overload
    async def playoff_series(self, **params: Unpack[NbaPlayoffSeriesDefaultParams]) -> NbaPlayoffSeriesResponse: ...
    @overload
    async def pt_defend(self, **params: Unpack[NbaPtDefendStreamParams]) -> BinaryIO: ...
    @overload
    async def pt_defend(self, **params: Unpack[NbaPtDefendTextResponseParams]) -> str: ...
    @overload
    async def pt_defend(self, **params: Unpack[NbaPtDefendDefaultParams]) -> NbaPtDefendResponse: ...
    @overload
    async def pt_stats(self, **params: Unpack[NbaPtStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def pt_stats(self, **params: Unpack[NbaPtStatsTextResponseParams]) -> str: ...
    @overload
    async def pt_stats(self, **params: Unpack[NbaPtStatsDefaultParams]) -> NbaPtStatsResponse: ...
    @overload
    async def scoreboard(self, **params: Unpack[NbaScoreboardStreamParams]) -> BinaryIO: ...
    @overload
    async def scoreboard(self, **params: Unpack[NbaScoreboardTextResponseParams]) -> str: ...
    @overload
    async def scoreboard(self, **params: Unpack[NbaScoreboardDefaultParams]) -> NbaScoreboardResponse: ...
    @overload
    async def shot_chart(self, **params: Unpack[NbaShotChartStreamParams]) -> BinaryIO: ...
    @overload
    async def shot_chart(self, **params: Unpack[NbaShotChartTextResponseParams]) -> str: ...
    @overload
    async def shot_chart(self, **params: Unpack[NbaShotChartDefaultParams]) -> NbaShotChartResponse: ...
    @overload
    async def standings(self, **params: Unpack[NbaStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[NbaStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[NbaStandingsDefaultParams]) -> NbaStandingsResponse: ...
    @overload
    async def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesTextResponseParams]) -> str: ...
    @overload
    async def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesDefaultParams]) -> NbaSynergyPlayTypesResponse: ...
    @overload
    async def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchDefaultParams]) -> NbaTeamDashByClutchResponse: ...
    @overload
    async def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsDefaultParams]) -> NbaTeamDashByGameSplitsResponse: ...
    @overload
    async def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesDefaultParams]) -> NbaTeamDashByLastNGamesResponse: ...
    @overload
    async def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentDefaultParams]) -> NbaTeamDashByOpponentResponse: ...
    @overload
    async def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassTextResponseParams]) -> str: ...
    @overload
    async def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassDefaultParams]) -> NbaTeamDashPtPassResponse: ...
    @overload
    async def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebTextResponseParams]) -> str: ...
    @overload
    async def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebDefaultParams]) -> NbaTeamDashPtRebResponse: ...
    @overload
    async def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsTextResponseParams]) -> str: ...
    @overload
    async def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsDefaultParams]) -> NbaTeamDashPtShotsResponse: ...
    @overload
    async def team_details(self, **params: Unpack[NbaTeamDetailsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_details(self, **params: Unpack[NbaTeamDetailsTextResponseParams]) -> str: ...
    @overload
    async def team_details(self, **params: Unpack[NbaTeamDetailsDefaultParams]) -> NbaTeamDetailsResponse: ...
    @overload
    async def team_game_logs(self, **params: Unpack[NbaTeamGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_game_logs(self, **params: Unpack[NbaTeamGameLogsTextResponseParams]) -> str: ...
    @overload
    async def team_game_logs(self, **params: Unpack[NbaTeamGameLogsDefaultParams]) -> NbaTeamGameLogsResponse: ...
    @overload
    async def team_info_common(self, **params: Unpack[NbaTeamInfoCommonStreamParams]) -> BinaryIO: ...
    @overload
    async def team_info_common(self, **params: Unpack[NbaTeamInfoCommonTextResponseParams]) -> str: ...
    @overload
    async def team_info_common(self, **params: Unpack[NbaTeamInfoCommonDefaultParams]) -> NbaTeamInfoCommonResponse: ...
    @overload
    async def team_on_off(self, **params: Unpack[NbaTeamOnOffStreamParams]) -> BinaryIO: ...
    @overload
    async def team_on_off(self, **params: Unpack[NbaTeamOnOffTextResponseParams]) -> str: ...
    @overload
    async def team_on_off(self, **params: Unpack[NbaTeamOnOffDefaultParams]) -> NbaTeamOnOffResponse: ...
    @overload
    async def team_pt_shot(self, **params: Unpack[NbaTeamPtShotStreamParams]) -> BinaryIO: ...
    @overload
    async def team_pt_shot(self, **params: Unpack[NbaTeamPtShotTextResponseParams]) -> str: ...
    @overload
    async def team_pt_shot(self, **params: Unpack[NbaTeamPtShotDefaultParams]) -> NbaTeamPtShotResponse: ...
    @overload
    async def team_roster(self, **params: Unpack[NbaTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    async def team_roster(self, **params: Unpack[NbaTeamRosterTextResponseParams]) -> str: ...
    @overload
    async def team_roster(self, **params: Unpack[NbaTeamRosterDefaultParams]) -> NbaTeamRosterResponse: ...
    @overload
    async def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsTextResponseParams]) -> str: ...
    @overload
    async def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsDefaultParams]) -> NbaTeamShotLocationsResponse: ...
    @overload
    async def team_stats(self, **params: Unpack[NbaTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_stats(self, **params: Unpack[NbaTeamStatsTextResponseParams]) -> str: ...
    @overload
    async def team_stats(self, **params: Unpack[NbaTeamStatsDefaultParams]) -> NbaTeamStatsResponse: ...
    @overload
    async def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersTextResponseParams]) -> str: ...
    @overload
    async def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersDefaultParams]) -> NbaTeamStatsLeadersResponse: ...
    @overload
    async def team_years(self, **params: Unpack[NbaTeamYearsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_years(self, **params: Unpack[NbaTeamYearsTextResponseParams]) -> str: ...
    @overload
    async def team_years(self, **params: Unpack[NbaTeamYearsDefaultParams]) -> NbaTeamYearsResponse: ...

class _AsyncNbaGroup:
    @overload
    async def box_score(self, **params: Unpack[NbaBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score(self, **params: Unpack[NbaBoxScoreTextResponseParams]) -> str: ...
    @overload
    async def box_score(self, **params: Unpack[NbaBoxScoreDefaultParams]) -> NbaBoxScoreResponse: ...
    @overload
    async def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedTextResponseParams]) -> str: ...
    @overload
    async def box_score_advanced(self, **params: Unpack[NbaBoxScoreAdvancedDefaultParams]) -> NbaBoxScoreAdvancedResponse: ...
    @overload
    async def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveTextResponseParams]) -> str: ...
    @overload
    async def box_score_defensive(self, **params: Unpack[NbaBoxScoreDefensiveDefaultParams]) -> NbaBoxScoreDefensiveResponse: ...
    @overload
    async def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsTextResponseParams]) -> str: ...
    @overload
    async def box_score_four_factors(self, **params: Unpack[NbaBoxScoreFourFactorsDefaultParams]) -> NbaBoxScoreFourFactorsResponse: ...
    @overload
    async def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscTextResponseParams]) -> str: ...
    @overload
    async def box_score_misc(self, **params: Unpack[NbaBoxScoreMiscDefaultParams]) -> NbaBoxScoreMiscResponse: ...
    @overload
    async def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackTextResponseParams]) -> str: ...
    @overload
    async def box_score_player_track(self, **params: Unpack[NbaBoxScorePlayerTrackDefaultParams]) -> NbaBoxScorePlayerTrackResponse: ...
    @overload
    async def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringTextResponseParams]) -> str: ...
    @overload
    async def box_score_scoring(self, **params: Unpack[NbaBoxScoreScoringDefaultParams]) -> NbaBoxScoreScoringResponse: ...
    @overload
    async def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryTextResponseParams]) -> str: ...
    @overload
    async def box_score_summary(self, **params: Unpack[NbaBoxScoreSummaryDefaultParams]) -> NbaBoxScoreSummaryResponse: ...
    @overload
    async def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageStreamParams]) -> BinaryIO: ...
    @overload
    async def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageTextResponseParams]) -> str: ...
    @overload
    async def box_score_usage(self, **params: Unpack[NbaBoxScoreUsageDefaultParams]) -> NbaBoxScoreUsageResponse: ...
    @overload
    async def common_all_players(self, **params: Unpack[NbaCommonAllPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def common_all_players(self, **params: Unpack[NbaCommonAllPlayersTextResponseParams]) -> str: ...
    @overload
    async def common_all_players(self, **params: Unpack[NbaCommonAllPlayersDefaultParams]) -> NbaCommonAllPlayersResponse: ...
    @overload
    async def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroStreamParams]) -> BinaryIO: ...
    @overload
    async def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroTextResponseParams]) -> str: ...
    @overload
    async def draft_combine_anthro(self, **params: Unpack[NbaDraftCombineAnthroDefaultParams]) -> NbaDraftCombineAnthroResponse: ...
    @overload
    async def enums(self, **params: Unpack[NbaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[NbaEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[NbaEnumsDefaultParams]) -> NbaEnumsResponse: ...
    @overload
    async def franchise_history(self, **params: Unpack[NbaFranchiseHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def franchise_history(self, **params: Unpack[NbaFranchiseHistoryTextResponseParams]) -> str: ...
    @overload
    async def franchise_history(self, **params: Unpack[NbaFranchiseHistoryDefaultParams]) -> NbaFranchiseHistoryResponse: ...
    @overload
    async def game_detail(self, **params: Unpack[NbaGameDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def game_detail(self, **params: Unpack[NbaGameDetailTextResponseParams]) -> str: ...
    @overload
    async def game_detail(self, **params: Unpack[NbaGameDetailDefaultParams]) -> NbaGameDetailResponse: ...
    @overload
    async def games(self, **params: Unpack[NbaGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[NbaGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[NbaGamesDefaultParams]) -> NbaGamesResponse: ...
    @overload
    async def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersStreamParams]) -> BinaryIO: ...
    @overload
    async def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersTextResponseParams]) -> str: ...
    @overload
    async def homepage_leaders(self, **params: Unpack[NbaHomepageLeadersDefaultParams]) -> NbaHomepageLeadersResponse: ...
    @overload
    async def homepage_v2(self, **params: Unpack[NbaHomepageV2StreamParams]) -> BinaryIO: ...
    @overload
    async def homepage_v2(self, **params: Unpack[NbaHomepageV2TextResponseParams]) -> str: ...
    @overload
    async def homepage_v2(self, **params: Unpack[NbaHomepageV2DefaultParams]) -> NbaHomepageV2Response: ...
    @overload
    async def hustle_player(self, **params: Unpack[NbaHustlePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def hustle_player(self, **params: Unpack[NbaHustlePlayerTextResponseParams]) -> str: ...
    @overload
    async def hustle_player(self, **params: Unpack[NbaHustlePlayerDefaultParams]) -> NbaHustlePlayerResponse: ...
    @overload
    async def hustle_stats(self, **params: Unpack[NbaHustleStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def hustle_stats(self, **params: Unpack[NbaHustleStatsTextResponseParams]) -> str: ...
    @overload
    async def hustle_stats(self, **params: Unpack[NbaHustleStatsDefaultParams]) -> NbaHustleStatsResponse: ...
    @overload
    async def hustle_team(self, **params: Unpack[NbaHustleTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def hustle_team(self, **params: Unpack[NbaHustleTeamTextResponseParams]) -> str: ...
    @overload
    async def hustle_team(self, **params: Unpack[NbaHustleTeamDefaultParams]) -> NbaHustleTeamResponse: ...
    @overload
    async def league_game_log(self, **params: Unpack[NbaLeagueGameLogStreamParams]) -> BinaryIO: ...
    @overload
    async def league_game_log(self, **params: Unpack[NbaLeagueGameLogTextResponseParams]) -> str: ...
    @overload
    async def league_game_log(self, **params: Unpack[NbaLeagueGameLogDefaultParams]) -> NbaLeagueGameLogResponse: ...
    @overload
    async def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartTextResponseParams]) -> str: ...
    @overload
    async def lineup_shot_chart(self, **params: Unpack[NbaLineupShotChartDefaultParams]) -> NbaLineupShotChartResponse: ...
    @overload
    async def lineups(self, **params: Unpack[NbaLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def lineups(self, **params: Unpack[NbaLineupsTextResponseParams]) -> str: ...
    @overload
    async def lineups(self, **params: Unpack[NbaLineupsDefaultParams]) -> NbaLineupsResponse: ...
    @overload
    async def news(self, **params: Unpack[NbaNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[NbaNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[NbaNewsDefaultParams]) -> NbaNewsResponse: ...
    @overload
    async def opp_pt_shot(self, **params: Unpack[NbaOppPtShotStreamParams]) -> BinaryIO: ...
    @overload
    async def opp_pt_shot(self, **params: Unpack[NbaOppPtShotTextResponseParams]) -> str: ...
    @overload
    async def opp_pt_shot(self, **params: Unpack[NbaOppPtShotDefaultParams]) -> NbaOppPtShotResponse: ...
    @overload
    async def play_by_play(self, **params: Unpack[NbaPlayByPlayStreamParams]) -> BinaryIO: ...
    @overload
    async def play_by_play(self, **params: Unpack[NbaPlayByPlayTextResponseParams]) -> str: ...
    @overload
    async def play_by_play(self, **params: Unpack[NbaPlayByPlayDefaultParams]) -> NbaPlayByPlayResponse: ...
    @overload
    async def player_awards(self, **params: Unpack[NbaPlayerAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_awards(self, **params: Unpack[NbaPlayerAwardsTextResponseParams]) -> str: ...
    @overload
    async def player_awards(self, **params: Unpack[NbaPlayerAwardsDefaultParams]) -> NbaPlayerAwardsResponse: ...
    @overload
    async def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsTextResponseParams]) -> str: ...
    @overload
    async def player_bio_stats(self, **params: Unpack[NbaPlayerBioStatsDefaultParams]) -> NbaPlayerBioStatsResponse: ...
    @overload
    async def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_career_stats(self, **params: Unpack[NbaPlayerCareerStatsDefaultParams]) -> NbaPlayerCareerStatsResponse: ...
    @overload
    async def player_clutch(self, **params: Unpack[NbaPlayerClutchStreamParams]) -> BinaryIO: ...
    @overload
    async def player_clutch(self, **params: Unpack[NbaPlayerClutchTextResponseParams]) -> str: ...
    @overload
    async def player_clutch(self, **params: Unpack[NbaPlayerClutchDefaultParams]) -> NbaPlayerClutchResponse: ...
    @overload
    async def player_compare(self, **params: Unpack[NbaPlayerCompareStreamParams]) -> BinaryIO: ...
    @overload
    async def player_compare(self, **params: Unpack[NbaPlayerCompareTextResponseParams]) -> str: ...
    @overload
    async def player_compare(self, **params: Unpack[NbaPlayerCompareDefaultParams]) -> NbaPlayerCompareResponse: ...
    @overload
    async def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_clutch(self, **params: Unpack[NbaPlayerDashByClutchDefaultParams]) -> NbaPlayerDashByClutchResponse: ...
    @overload
    async def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_game_splits(self, **params: Unpack[NbaPlayerDashByGameSplitsDefaultParams]) -> NbaPlayerDashByGameSplitsResponse: ...
    @overload
    async def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_last_n_games(self, **params: Unpack[NbaPlayerDashByLastNGamesDefaultParams]) -> NbaPlayerDashByLastNGamesResponse: ...
    @overload
    async def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentTextResponseParams]) -> str: ...
    @overload
    async def player_dash_by_opponent(self, **params: Unpack[NbaPlayerDashByOpponentDefaultParams]) -> NbaPlayerDashByOpponentResponse: ...
    @overload
    async def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassTextResponseParams]) -> str: ...
    @overload
    async def player_dash_pt_pass(self, **params: Unpack[NbaPlayerDashPtPassDefaultParams]) -> NbaPlayerDashPtPassResponse: ...
    @overload
    async def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebTextResponseParams]) -> str: ...
    @overload
    async def player_dash_pt_reb(self, **params: Unpack[NbaPlayerDashPtRebDefaultParams]) -> NbaPlayerDashPtRebResponse: ...
    @overload
    async def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsTextResponseParams]) -> str: ...
    @overload
    async def player_dash_pt_shots(self, **params: Unpack[NbaPlayerDashPtShotsDefaultParams]) -> NbaPlayerDashPtShotsResponse: ...
    @overload
    async def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsTextResponseParams]) -> str: ...
    @overload
    async def player_game_logs(self, **params: Unpack[NbaPlayerGameLogsDefaultParams]) -> NbaPlayerGameLogsResponse: ...
    @overload
    async def player_info(self, **params: Unpack[NbaPlayerInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def player_info(self, **params: Unpack[NbaPlayerInfoTextResponseParams]) -> str: ...
    @overload
    async def player_info(self, **params: Unpack[NbaPlayerInfoDefaultParams]) -> NbaPlayerInfoResponse: ...
    @overload
    async def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2StreamParams]) -> BinaryIO: ...
    @overload
    async def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2TextResponseParams]) -> str: ...
    @overload
    async def player_profile_v2(self, **params: Unpack[NbaPlayerProfileV2DefaultParams]) -> NbaPlayerProfileV2Response: ...
    @overload
    async def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotStreamParams]) -> BinaryIO: ...
    @overload
    async def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotTextResponseParams]) -> str: ...
    @overload
    async def player_pt_shot(self, **params: Unpack[NbaPlayerPtShotDefaultParams]) -> NbaPlayerPtShotResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[NbaPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[NbaPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[NbaPlayerStatsDefaultParams]) -> NbaPlayerStatsResponse: ...
    @overload
    async def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderStreamParams]) -> BinaryIO: ...
    @overload
    async def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderTextResponseParams]) -> str: ...
    @overload
    async def player_streak_finder(self, **params: Unpack[NbaPlayerStreakFinderDefaultParams]) -> NbaPlayerStreakFinderResponse: ...
    @overload
    async def players(self, **params: Unpack[NbaPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def players(self, **params: Unpack[NbaPlayersTextResponseParams]) -> str: ...
    @overload
    async def players(self, **params: Unpack[NbaPlayersDefaultParams]) -> NbaPlayersResponse: ...
    @overload
    async def playoff_picture(self, **params: Unpack[NbaPlayoffPictureStreamParams]) -> BinaryIO: ...
    @overload
    async def playoff_picture(self, **params: Unpack[NbaPlayoffPictureTextResponseParams]) -> str: ...
    @overload
    async def playoff_picture(self, **params: Unpack[NbaPlayoffPictureDefaultParams]) -> NbaPlayoffPictureResponse: ...
    @overload
    async def playoff_series(self, **params: Unpack[NbaPlayoffSeriesStreamParams]) -> BinaryIO: ...
    @overload
    async def playoff_series(self, **params: Unpack[NbaPlayoffSeriesTextResponseParams]) -> str: ...
    @overload
    async def playoff_series(self, **params: Unpack[NbaPlayoffSeriesDefaultParams]) -> NbaPlayoffSeriesResponse: ...
    @overload
    async def pt_defend(self, **params: Unpack[NbaPtDefendStreamParams]) -> BinaryIO: ...
    @overload
    async def pt_defend(self, **params: Unpack[NbaPtDefendTextResponseParams]) -> str: ...
    @overload
    async def pt_defend(self, **params: Unpack[NbaPtDefendDefaultParams]) -> NbaPtDefendResponse: ...
    @overload
    async def pt_stats(self, **params: Unpack[NbaPtStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def pt_stats(self, **params: Unpack[NbaPtStatsTextResponseParams]) -> str: ...
    @overload
    async def pt_stats(self, **params: Unpack[NbaPtStatsDefaultParams]) -> NbaPtStatsResponse: ...
    @overload
    async def scoreboard(self, **params: Unpack[NbaScoreboardStreamParams]) -> BinaryIO: ...
    @overload
    async def scoreboard(self, **params: Unpack[NbaScoreboardTextResponseParams]) -> str: ...
    @overload
    async def scoreboard(self, **params: Unpack[NbaScoreboardDefaultParams]) -> NbaScoreboardResponse: ...
    @overload
    async def shot_chart(self, **params: Unpack[NbaShotChartStreamParams]) -> BinaryIO: ...
    @overload
    async def shot_chart(self, **params: Unpack[NbaShotChartTextResponseParams]) -> str: ...
    @overload
    async def shot_chart(self, **params: Unpack[NbaShotChartDefaultParams]) -> NbaShotChartResponse: ...
    @overload
    async def standings(self, **params: Unpack[NbaStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[NbaStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[NbaStandingsDefaultParams]) -> NbaStandingsResponse: ...
    @overload
    async def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesTextResponseParams]) -> str: ...
    @overload
    async def synergy_play_types(self, **params: Unpack[NbaSynergyPlayTypesDefaultParams]) -> NbaSynergyPlayTypesResponse: ...
    @overload
    async def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_clutch(self, **params: Unpack[NbaTeamDashByClutchDefaultParams]) -> NbaTeamDashByClutchResponse: ...
    @overload
    async def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_game_splits(self, **params: Unpack[NbaTeamDashByGameSplitsDefaultParams]) -> NbaTeamDashByGameSplitsResponse: ...
    @overload
    async def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_last_n_games(self, **params: Unpack[NbaTeamDashByLastNGamesDefaultParams]) -> NbaTeamDashByLastNGamesResponse: ...
    @overload
    async def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentTextResponseParams]) -> str: ...
    @overload
    async def team_dash_by_opponent(self, **params: Unpack[NbaTeamDashByOpponentDefaultParams]) -> NbaTeamDashByOpponentResponse: ...
    @overload
    async def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassTextResponseParams]) -> str: ...
    @overload
    async def team_dash_pt_pass(self, **params: Unpack[NbaTeamDashPtPassDefaultParams]) -> NbaTeamDashPtPassResponse: ...
    @overload
    async def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebTextResponseParams]) -> str: ...
    @overload
    async def team_dash_pt_reb(self, **params: Unpack[NbaTeamDashPtRebDefaultParams]) -> NbaTeamDashPtRebResponse: ...
    @overload
    async def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsTextResponseParams]) -> str: ...
    @overload
    async def team_dash_pt_shots(self, **params: Unpack[NbaTeamDashPtShotsDefaultParams]) -> NbaTeamDashPtShotsResponse: ...
    @overload
    async def team_details(self, **params: Unpack[NbaTeamDetailsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_details(self, **params: Unpack[NbaTeamDetailsTextResponseParams]) -> str: ...
    @overload
    async def team_details(self, **params: Unpack[NbaTeamDetailsDefaultParams]) -> NbaTeamDetailsResponse: ...
    @overload
    async def team_game_logs(self, **params: Unpack[NbaTeamGameLogsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_game_logs(self, **params: Unpack[NbaTeamGameLogsTextResponseParams]) -> str: ...
    @overload
    async def team_game_logs(self, **params: Unpack[NbaTeamGameLogsDefaultParams]) -> NbaTeamGameLogsResponse: ...
    @overload
    async def team_info_common(self, **params: Unpack[NbaTeamInfoCommonStreamParams]) -> BinaryIO: ...
    @overload
    async def team_info_common(self, **params: Unpack[NbaTeamInfoCommonTextResponseParams]) -> str: ...
    @overload
    async def team_info_common(self, **params: Unpack[NbaTeamInfoCommonDefaultParams]) -> NbaTeamInfoCommonResponse: ...
    @overload
    async def team_on_off(self, **params: Unpack[NbaTeamOnOffStreamParams]) -> BinaryIO: ...
    @overload
    async def team_on_off(self, **params: Unpack[NbaTeamOnOffTextResponseParams]) -> str: ...
    @overload
    async def team_on_off(self, **params: Unpack[NbaTeamOnOffDefaultParams]) -> NbaTeamOnOffResponse: ...
    @overload
    async def team_pt_shot(self, **params: Unpack[NbaTeamPtShotStreamParams]) -> BinaryIO: ...
    @overload
    async def team_pt_shot(self, **params: Unpack[NbaTeamPtShotTextResponseParams]) -> str: ...
    @overload
    async def team_pt_shot(self, **params: Unpack[NbaTeamPtShotDefaultParams]) -> NbaTeamPtShotResponse: ...
    @overload
    async def team_roster(self, **params: Unpack[NbaTeamRosterStreamParams]) -> BinaryIO: ...
    @overload
    async def team_roster(self, **params: Unpack[NbaTeamRosterTextResponseParams]) -> str: ...
    @overload
    async def team_roster(self, **params: Unpack[NbaTeamRosterDefaultParams]) -> NbaTeamRosterResponse: ...
    @overload
    async def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsTextResponseParams]) -> str: ...
    @overload
    async def team_shot_locations(self, **params: Unpack[NbaTeamShotLocationsDefaultParams]) -> NbaTeamShotLocationsResponse: ...
    @overload
    async def team_stats(self, **params: Unpack[NbaTeamStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_stats(self, **params: Unpack[NbaTeamStatsTextResponseParams]) -> str: ...
    @overload
    async def team_stats(self, **params: Unpack[NbaTeamStatsDefaultParams]) -> NbaTeamStatsResponse: ...
    @overload
    async def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersTextResponseParams]) -> str: ...
    @overload
    async def team_stats_leaders(self, **params: Unpack[NbaTeamStatsLeadersDefaultParams]) -> NbaTeamStatsLeadersResponse: ...
    @overload
    async def team_years(self, **params: Unpack[NbaTeamYearsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_years(self, **params: Unpack[NbaTeamYearsTextResponseParams]) -> str: ...
    @overload
    async def team_years(self, **params: Unpack[NbaTeamYearsDefaultParams]) -> NbaTeamYearsResponse: ...

NbaBoxScoreDefaultParams = TypedDict('NbaBoxScoreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreTextResponseParams = TypedDict('NbaBoxScoreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreStreamParams = TypedDict('NbaBoxScoreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreAdvancedDefaultParams = TypedDict('NbaBoxScoreAdvancedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreAdvancedTextResponseParams = TypedDict('NbaBoxScoreAdvancedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreAdvancedStreamParams = TypedDict('NbaBoxScoreAdvancedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreDefensiveDefaultParams = TypedDict('NbaBoxScoreDefensiveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreDefensiveTextResponseParams = TypedDict('NbaBoxScoreDefensiveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreDefensiveStreamParams = TypedDict('NbaBoxScoreDefensiveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreFourFactorsDefaultParams = TypedDict('NbaBoxScoreFourFactorsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreFourFactorsTextResponseParams = TypedDict('NbaBoxScoreFourFactorsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreFourFactorsStreamParams = TypedDict('NbaBoxScoreFourFactorsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreMiscDefaultParams = TypedDict('NbaBoxScoreMiscDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreMiscTextResponseParams = TypedDict('NbaBoxScoreMiscTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreMiscStreamParams = TypedDict('NbaBoxScoreMiscStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScorePlayerTrackDefaultParams = TypedDict('NbaBoxScorePlayerTrackDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScorePlayerTrackTextResponseParams = TypedDict('NbaBoxScorePlayerTrackTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScorePlayerTrackStreamParams = TypedDict('NbaBoxScorePlayerTrackStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreScoringDefaultParams = TypedDict('NbaBoxScoreScoringDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreScoringTextResponseParams = TypedDict('NbaBoxScoreScoringTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreScoringStreamParams = TypedDict('NbaBoxScoreScoringStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreSummaryDefaultParams = TypedDict('NbaBoxScoreSummaryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreSummaryTextResponseParams = TypedDict('NbaBoxScoreSummaryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreSummaryStreamParams = TypedDict('NbaBoxScoreSummaryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
}, total=False)

NbaBoxScoreUsageDefaultParams = TypedDict('NbaBoxScoreUsageDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreUsageTextResponseParams = TypedDict('NbaBoxScoreUsageTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaBoxScoreUsageStreamParams = TypedDict('NbaBoxScoreUsageStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'league_id': NotRequired[Literal['00']],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaCommonAllPlayersDefaultParams = TypedDict('NbaCommonAllPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'is_only_current_season': NotRequired[bool],
}, total=False)

NbaCommonAllPlayersTextResponseParams = TypedDict('NbaCommonAllPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'is_only_current_season': NotRequired[bool],
}, total=False)

NbaCommonAllPlayersStreamParams = TypedDict('NbaCommonAllPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'is_only_current_season': NotRequired[bool],
}, total=False)

NbaDraftCombineAnthroDefaultParams = TypedDict('NbaDraftCombineAnthroDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'season_year': Required[str],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaDraftCombineAnthroTextResponseParams = TypedDict('NbaDraftCombineAnthroTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'season_year': Required[str],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaDraftCombineAnthroStreamParams = TypedDict('NbaDraftCombineAnthroStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'season_year': Required[str],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaEnumsDefaultParams = TypedDict('NbaEnumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

NbaEnumsTextResponseParams = TypedDict('NbaEnumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

NbaEnumsStreamParams = TypedDict('NbaEnumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

NbaFranchiseHistoryDefaultParams = TypedDict('NbaFranchiseHistoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'team_id': NotRequired[int],
}, total=False)

NbaFranchiseHistoryTextResponseParams = TypedDict('NbaFranchiseHistoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'team_id': NotRequired[int],
}, total=False)

NbaFranchiseHistoryStreamParams = TypedDict('NbaFranchiseHistoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'team_id': NotRequired[int],
}, total=False)

NbaGameDetailDefaultParams = TypedDict('NbaGameDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
}, total=False)

NbaGameDetailTextResponseParams = TypedDict('NbaGameDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
}, total=False)

NbaGameDetailStreamParams = TypedDict('NbaGameDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
}, total=False)

NbaGamesDefaultParams = TypedDict('NbaGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

NbaGamesTextResponseParams = TypedDict('NbaGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

NbaGamesStreamParams = TypedDict('NbaGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

NbaHomepageLeadersDefaultParams = TypedDict('NbaHomepageLeadersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'stat_category': NotRequired[Literal['Points', 'Rebounds']],
    'player_or_team': NotRequired[Literal['Team']],
    'player_scope': NotRequired[str],
    'game_scope': NotRequired[Literal['Season']],
}, total=False)

NbaHomepageLeadersTextResponseParams = TypedDict('NbaHomepageLeadersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'stat_category': NotRequired[Literal['Points', 'Rebounds']],
    'player_or_team': NotRequired[Literal['Team']],
    'player_scope': NotRequired[str],
    'game_scope': NotRequired[Literal['Season']],
}, total=False)

NbaHomepageLeadersStreamParams = TypedDict('NbaHomepageLeadersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'stat_category': NotRequired[Literal['Points', 'Rebounds']],
    'player_or_team': NotRequired[Literal['Team']],
    'player_scope': NotRequired[str],
    'game_scope': NotRequired[Literal['Season']],
}, total=False)

NbaHomepageV2DefaultParams = TypedDict('NbaHomepageV2DefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'game_scope': NotRequired[Literal['Season']],
    'player_scope': NotRequired[str],
    'player_or_team': NotRequired[Literal['Player']],
    'stat_type': NotRequired[Literal['Traditional']],
}, total=False)

NbaHomepageV2TextResponseParams = TypedDict('NbaHomepageV2TextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'game_scope': NotRequired[Literal['Season']],
    'player_scope': NotRequired[str],
    'player_or_team': NotRequired[Literal['Player']],
    'stat_type': NotRequired[Literal['Traditional']],
}, total=False)

NbaHomepageV2StreamParams = TypedDict('NbaHomepageV2StreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'game_scope': NotRequired[Literal['Season']],
    'player_scope': NotRequired[str],
    'player_or_team': NotRequired[Literal['Player']],
    'stat_type': NotRequired[Literal['Traditional']],
}, total=False)

NbaHustlePlayerDefaultParams = TypedDict('NbaHustlePlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaHustlePlayerTextResponseParams = TypedDict('NbaHustlePlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaHustlePlayerStreamParams = TypedDict('NbaHustlePlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaHustleStatsDefaultParams = TypedDict('NbaHustleStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
}, total=False)

NbaHustleStatsTextResponseParams = TypedDict('NbaHustleStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
}, total=False)

NbaHustleStatsStreamParams = TypedDict('NbaHustleStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
}, total=False)

NbaHustleTeamDefaultParams = TypedDict('NbaHustleTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaHustleTeamTextResponseParams = TypedDict('NbaHustleTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaHustleTeamStreamParams = TypedDict('NbaHustleTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaLeagueGameLogDefaultParams = TypedDict('NbaLeagueGameLogDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'direction': NotRequired[Literal['DESC']],
    'player_or_team': NotRequired[Literal['T']],
    'sorter': NotRequired[Literal['DATE']],
}, total=False)

NbaLeagueGameLogTextResponseParams = TypedDict('NbaLeagueGameLogTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'direction': NotRequired[Literal['DESC']],
    'player_or_team': NotRequired[Literal['T']],
    'sorter': NotRequired[Literal['DATE']],
}, total=False)

NbaLeagueGameLogStreamParams = TypedDict('NbaLeagueGameLogStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'direction': NotRequired[Literal['DESC']],
    'player_or_team': NotRequired[Literal['T']],
    'sorter': NotRequired[Literal['DATE']],
}, total=False)

NbaLineupShotChartDefaultParams = TypedDict('NbaLineupShotChartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
    'group_quantity': NotRequired[Literal['5']],
    'period': NotRequired[int],
}, total=False)

NbaLineupShotChartTextResponseParams = TypedDict('NbaLineupShotChartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
    'group_quantity': NotRequired[Literal['5']],
    'period': NotRequired[int],
}, total=False)

NbaLineupShotChartStreamParams = TypedDict('NbaLineupShotChartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
    'group_quantity': NotRequired[Literal['5']],
    'period': NotRequired[int],
}, total=False)

NbaLineupsDefaultParams = TypedDict('NbaLineupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'group_quantity': NotRequired[Literal['5']],
}, total=False)

NbaLineupsTextResponseParams = TypedDict('NbaLineupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'group_quantity': NotRequired[Literal['5']],
}, total=False)

NbaLineupsStreamParams = TypedDict('NbaLineupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'group_quantity': NotRequired[Literal['5']],
}, total=False)

NbaNewsDefaultParams = TypedDict('NbaNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

NbaNewsTextResponseParams = TypedDict('NbaNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

NbaNewsStreamParams = TypedDict('NbaNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

NbaOppPtShotDefaultParams = TypedDict('NbaOppPtShotDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaOppPtShotTextResponseParams = TypedDict('NbaOppPtShotTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaOppPtShotStreamParams = TypedDict('NbaOppPtShotStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayByPlayDefaultParams = TypedDict('NbaPlayByPlayDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaPlayByPlayTextResponseParams = TypedDict('NbaPlayByPlayTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaPlayByPlayStreamParams = TypedDict('NbaPlayByPlayStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'start_period': NotRequired[int],
    'end_period': NotRequired[int],
}, total=False)

NbaPlayerAwardsDefaultParams = TypedDict('NbaPlayerAwardsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
}, total=False)

NbaPlayerAwardsTextResponseParams = TypedDict('NbaPlayerAwardsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
}, total=False)

NbaPlayerAwardsStreamParams = TypedDict('NbaPlayerAwardsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
}, total=False)

NbaPlayerBioStatsDefaultParams = TypedDict('NbaPlayerBioStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerBioStatsTextResponseParams = TypedDict('NbaPlayerBioStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerBioStatsStreamParams = TypedDict('NbaPlayerBioStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerCareerStatsDefaultParams = TypedDict('NbaPlayerCareerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame']],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerCareerStatsTextResponseParams = TypedDict('NbaPlayerCareerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame']],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerCareerStatsStreamParams = TypedDict('NbaPlayerCareerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame']],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerClutchDefaultParams = TypedDict('NbaPlayerClutchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'clutch_time': NotRequired[Literal['Last 5 Minutes']],
    'ahead_behind': NotRequired[Literal['Ahead or Behind']],
    'point_diff': NotRequired[Literal['5']],
}, total=False)

NbaPlayerClutchTextResponseParams = TypedDict('NbaPlayerClutchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'clutch_time': NotRequired[Literal['Last 5 Minutes']],
    'ahead_behind': NotRequired[Literal['Ahead or Behind']],
    'point_diff': NotRequired[Literal['5']],
}, total=False)

NbaPlayerClutchStreamParams = TypedDict('NbaPlayerClutchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'clutch_time': NotRequired[Literal['Last 5 Minutes']],
    'ahead_behind': NotRequired[Literal['Ahead or Behind']],
    'point_diff': NotRequired[Literal['5']],
}, total=False)

NbaPlayerCompareDefaultParams = TypedDict('NbaPlayerCompareDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_ids': Required[list[str]],
    'vs_player_ids': Required[list[str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerCompareTextResponseParams = TypedDict('NbaPlayerCompareTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_ids': Required[list[str]],
    'vs_player_ids': Required[list[str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerCompareStreamParams = TypedDict('NbaPlayerCompareStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_ids': Required[list[str]],
    'vs_player_ids': Required[list[str]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByClutchDefaultParams = TypedDict('NbaPlayerDashByClutchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByClutchTextResponseParams = TypedDict('NbaPlayerDashByClutchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByClutchStreamParams = TypedDict('NbaPlayerDashByClutchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByGameSplitsDefaultParams = TypedDict('NbaPlayerDashByGameSplitsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByGameSplitsTextResponseParams = TypedDict('NbaPlayerDashByGameSplitsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByGameSplitsStreamParams = TypedDict('NbaPlayerDashByGameSplitsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByLastNGamesDefaultParams = TypedDict('NbaPlayerDashByLastNGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByLastNGamesTextResponseParams = TypedDict('NbaPlayerDashByLastNGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByLastNGamesStreamParams = TypedDict('NbaPlayerDashByLastNGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByOpponentDefaultParams = TypedDict('NbaPlayerDashByOpponentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByOpponentTextResponseParams = TypedDict('NbaPlayerDashByOpponentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashByOpponentStreamParams = TypedDict('NbaPlayerDashByOpponentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaPlayerDashPtPassDefaultParams = TypedDict('NbaPlayerDashPtPassDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtPassTextResponseParams = TypedDict('NbaPlayerDashPtPassTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtPassStreamParams = TypedDict('NbaPlayerDashPtPassStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtRebDefaultParams = TypedDict('NbaPlayerDashPtRebDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtRebTextResponseParams = TypedDict('NbaPlayerDashPtRebTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtRebStreamParams = TypedDict('NbaPlayerDashPtRebStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtShotsDefaultParams = TypedDict('NbaPlayerDashPtShotsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtShotsTextResponseParams = TypedDict('NbaPlayerDashPtShotsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerDashPtShotsStreamParams = TypedDict('NbaPlayerDashPtShotsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaPlayerGameLogsDefaultParams = TypedDict('NbaPlayerGameLogsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': Required[int],
}, total=False)

NbaPlayerGameLogsTextResponseParams = TypedDict('NbaPlayerGameLogsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': Required[int],
}, total=False)

NbaPlayerGameLogsStreamParams = TypedDict('NbaPlayerGameLogsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': Required[int],
}, total=False)

NbaPlayerInfoDefaultParams = TypedDict('NbaPlayerInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerInfoTextResponseParams = TypedDict('NbaPlayerInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerInfoStreamParams = TypedDict('NbaPlayerInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaPlayerProfileV2DefaultParams = TypedDict('NbaPlayerProfileV2DefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerProfileV2TextResponseParams = TypedDict('NbaPlayerProfileV2TextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerProfileV2StreamParams = TypedDict('NbaPlayerProfileV2StreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[int],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerPtShotDefaultParams = TypedDict('NbaPlayerPtShotDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerPtShotTextResponseParams = TypedDict('NbaPlayerPtShotTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerPtShotStreamParams = TypedDict('NbaPlayerPtShotStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerStatsDefaultParams = TypedDict('NbaPlayerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerStatsTextResponseParams = TypedDict('NbaPlayerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerStatsStreamParams = TypedDict('NbaPlayerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaPlayerStreakFinderDefaultParams = TypedDict('NbaPlayerStreakFinderDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': NotRequired[int],
    'min_games': NotRequired[int],
}, total=False)

NbaPlayerStreakFinderTextResponseParams = TypedDict('NbaPlayerStreakFinderTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': NotRequired[int],
    'min_games': NotRequired[int],
}, total=False)

NbaPlayerStreakFinderStreamParams = TypedDict('NbaPlayerStreakFinderStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'player_id': NotRequired[int],
    'min_games': NotRequired[int],
}, total=False)

NbaPlayersDefaultParams = TypedDict('NbaPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'team_id': NotRequired[int],
    'active': NotRequired[bool],
}, total=False)

NbaPlayersTextResponseParams = TypedDict('NbaPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'team_id': NotRequired[int],
    'active': NotRequired[bool],
}, total=False)

NbaPlayersStreamParams = TypedDict('NbaPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'team_id': NotRequired[int],
    'active': NotRequired[bool],
}, total=False)

NbaPlayoffPictureDefaultParams = TypedDict('NbaPlayoffPictureDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season_id': NotRequired[str],
}, total=False)

NbaPlayoffPictureTextResponseParams = TypedDict('NbaPlayoffPictureTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season_id': NotRequired[str],
}, total=False)

NbaPlayoffPictureStreamParams = TypedDict('NbaPlayoffPictureStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season_id': NotRequired[str],
}, total=False)

NbaPlayoffSeriesDefaultParams = TypedDict('NbaPlayoffSeriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaPlayoffSeriesTextResponseParams = TypedDict('NbaPlayoffSeriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaPlayoffSeriesStreamParams = TypedDict('NbaPlayoffSeriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaPtDefendDefaultParams = TypedDict('NbaPtDefendDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'defense_category': NotRequired[Literal['Overall', '3 Pointers']],
}, total=False)

NbaPtDefendTextResponseParams = TypedDict('NbaPtDefendTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'defense_category': NotRequired[Literal['Overall', '3 Pointers']],
}, total=False)

NbaPtDefendStreamParams = TypedDict('NbaPtDefendStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'defense_category': NotRequired[Literal['Overall', '3 Pointers']],
}, total=False)

NbaPtStatsDefaultParams = TypedDict('NbaPtStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'pt_measure_type': NotRequired[Literal['SpeedDistance']],
}, total=False)

NbaPtStatsTextResponseParams = TypedDict('NbaPtStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'pt_measure_type': NotRequired[Literal['SpeedDistance']],
}, total=False)

NbaPtStatsStreamParams = TypedDict('NbaPtStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'pt_measure_type': NotRequired[Literal['SpeedDistance']],
}, total=False)

NbaScoreboardDefaultParams = TypedDict('NbaScoreboardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'game_date': NotRequired[str],
    'day_offset': NotRequired[int],
}, total=False)

NbaScoreboardTextResponseParams = TypedDict('NbaScoreboardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'game_date': NotRequired[str],
    'day_offset': NotRequired[int],
}, total=False)

NbaScoreboardStreamParams = TypedDict('NbaScoreboardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'game_date': NotRequired[str],
    'day_offset': NotRequired[int],
}, total=False)

NbaShotChartDefaultParams = TypedDict('NbaShotChartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': NotRequired[int],
    'team_id': NotRequired[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
}, total=False)

NbaShotChartTextResponseParams = TypedDict('NbaShotChartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': NotRequired[int],
    'team_id': NotRequired[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
}, total=False)

NbaShotChartStreamParams = TypedDict('NbaShotChartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': NotRequired[int],
    'team_id': NotRequired[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'context_measure': NotRequired[Literal['FGA', 'FG_PCT']],
}, total=False)

NbaStandingsDefaultParams = TypedDict('NbaStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
}, total=False)

NbaStandingsTextResponseParams = TypedDict('NbaStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
}, total=False)

NbaStandingsStreamParams = TypedDict('NbaStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
}, total=False)

NbaSynergyPlayTypesDefaultParams = TypedDict('NbaSynergyPlayTypesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season_year': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'play_type': NotRequired[Literal['Isolation']],
    'per_mode': NotRequired[Literal['PerGame']],
    'player_or_team': NotRequired[Literal['T']],
    'type_grouping': NotRequired[Literal['offensive']],
}, total=False)

NbaSynergyPlayTypesTextResponseParams = TypedDict('NbaSynergyPlayTypesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season_year': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'play_type': NotRequired[Literal['Isolation']],
    'per_mode': NotRequired[Literal['PerGame']],
    'player_or_team': NotRequired[Literal['T']],
    'type_grouping': NotRequired[Literal['offensive']],
}, total=False)

NbaSynergyPlayTypesStreamParams = TypedDict('NbaSynergyPlayTypesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season_year': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'play_type': NotRequired[Literal['Isolation']],
    'per_mode': NotRequired[Literal['PerGame']],
    'player_or_team': NotRequired[Literal['T']],
    'type_grouping': NotRequired[Literal['offensive']],
}, total=False)

NbaTeamDashByClutchDefaultParams = TypedDict('NbaTeamDashByClutchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByClutchTextResponseParams = TypedDict('NbaTeamDashByClutchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByClutchStreamParams = TypedDict('NbaTeamDashByClutchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByGameSplitsDefaultParams = TypedDict('NbaTeamDashByGameSplitsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByGameSplitsTextResponseParams = TypedDict('NbaTeamDashByGameSplitsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByGameSplitsStreamParams = TypedDict('NbaTeamDashByGameSplitsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByLastNGamesDefaultParams = TypedDict('NbaTeamDashByLastNGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByLastNGamesTextResponseParams = TypedDict('NbaTeamDashByLastNGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByLastNGamesStreamParams = TypedDict('NbaTeamDashByLastNGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByOpponentDefaultParams = TypedDict('NbaTeamDashByOpponentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByOpponentTextResponseParams = TypedDict('NbaTeamDashByOpponentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashByOpponentStreamParams = TypedDict('NbaTeamDashByOpponentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
}, total=False)

NbaTeamDashPtPassDefaultParams = TypedDict('NbaTeamDashPtPassDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDashPtPassTextResponseParams = TypedDict('NbaTeamDashPtPassTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDashPtPassStreamParams = TypedDict('NbaTeamDashPtPassStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDashPtRebDefaultParams = TypedDict('NbaTeamDashPtRebDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaTeamDashPtRebTextResponseParams = TypedDict('NbaTeamDashPtRebTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaTeamDashPtRebStreamParams = TypedDict('NbaTeamDashPtRebStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'per_mode': NotRequired[Literal['PerGame']],
}, total=False)

NbaTeamDashPtShotsDefaultParams = TypedDict('NbaTeamDashPtShotsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDashPtShotsTextResponseParams = TypedDict('NbaTeamDashPtShotsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDashPtShotsStreamParams = TypedDict('NbaTeamDashPtShotsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'team_id': Required[int],
}, total=False)

NbaTeamDetailsDefaultParams = TypedDict('NbaTeamDetailsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaTeamDetailsTextResponseParams = TypedDict('NbaTeamDetailsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaTeamDetailsStreamParams = TypedDict('NbaTeamDetailsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaTeamGameLogsDefaultParams = TypedDict('NbaTeamGameLogsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamGameLogsTextResponseParams = TypedDict('NbaTeamGameLogsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamGameLogsStreamParams = TypedDict('NbaTeamGameLogsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamInfoCommonDefaultParams = TypedDict('NbaTeamInfoCommonDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamInfoCommonTextResponseParams = TypedDict('NbaTeamInfoCommonTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamInfoCommonStreamParams = TypedDict('NbaTeamInfoCommonStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'team_id': Required[int],
}, total=False)

NbaTeamOnOffDefaultParams = TypedDict('NbaTeamOnOffDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'team_id': Required[int],
}, total=False)

NbaTeamOnOffTextResponseParams = TypedDict('NbaTeamOnOffTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'team_id': Required[int],
}, total=False)

NbaTeamOnOffStreamParams = TypedDict('NbaTeamOnOffStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'team_id': Required[int],
}, total=False)

NbaTeamPtShotDefaultParams = TypedDict('NbaTeamPtShotDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamPtShotTextResponseParams = TypedDict('NbaTeamPtShotTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamPtShotStreamParams = TypedDict('NbaTeamPtShotStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamRosterDefaultParams = TypedDict('NbaTeamRosterDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaTeamRosterTextResponseParams = TypedDict('NbaTeamRosterTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaTeamRosterStreamParams = TypedDict('NbaTeamRosterStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
}, total=False)

NbaTeamShotLocationsDefaultParams = TypedDict('NbaTeamShotLocationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'distance_range': NotRequired[str],
}, total=False)

NbaTeamShotLocationsTextResponseParams = TypedDict('NbaTeamShotLocationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'distance_range': NotRequired[str],
}, total=False)

NbaTeamShotLocationsStreamParams = TypedDict('NbaTeamShotLocationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season']],
    'measure_type': NotRequired[Literal['Base']],
    'per_mode': NotRequired[Literal['PerGame']],
    'distance_range': NotRequired[str],
}, total=False)

NbaTeamStatsDefaultParams = TypedDict('NbaTeamStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamStatsTextResponseParams = TypedDict('NbaTeamStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamStatsStreamParams = TypedDict('NbaTeamStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'measure_type': NotRequired[Literal['Base', 'Advanced', 'Misc', 'Scoring', 'Defense', 'Opponent']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
}, total=False)

NbaTeamStatsLeadersDefaultParams = TypedDict('NbaTeamStatsLeadersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'stat_category': Required[Literal['PTS', 'REB', 'AST', 'BLK', 'STL', 'TOV']],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'scope': NotRequired[Literal['S']],
}, total=False)

NbaTeamStatsLeadersTextResponseParams = TypedDict('NbaTeamStatsLeadersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'stat_category': Required[Literal['PTS', 'REB', 'AST', 'BLK', 'STL', 'TOV']],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'scope': NotRequired[Literal['S']],
}, total=False)

NbaTeamStatsLeadersStreamParams = TypedDict('NbaTeamStatsLeadersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'stat_category': Required[Literal['PTS', 'REB', 'AST', 'BLK', 'STL', 'TOV']],
    'league_id': NotRequired[Literal['00']],
    'season': NotRequired[str],
    'season_type': NotRequired[Literal['Regular Season', 'Playoffs', 'Pre Season', 'All Star']],
    'per_mode': NotRequired[Literal['PerGame', 'Totals', 'Per36', 'Per48', 'Per100Possessions', 'MinutesPer', 'PerPossession']],
    'scope': NotRequired[Literal['S']],
}, total=False)

NbaTeamYearsDefaultParams = TypedDict('NbaTeamYearsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaTeamYearsTextResponseParams = TypedDict('NbaTeamYearsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': NotRequired[Literal['00']],
}, total=False)

NbaTeamYearsStreamParams = TypedDict('NbaTeamYearsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': NotRequired[Literal['00']],
}, total=False)
