# NBA clients for Crawlora

Official Crawlora client packages for the hosted NBA API. Access 70 API endpoints covering games, standings, player and team statistics, play-by-play, and dashboards from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape NBA locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by NBA or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/nba`](javascript/README.md)
- Python: [`crawlora-nba`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-nba`](go.mod)
- Ruby: [`crawlora-nba`](ruby/README.md)
- Java: [`net.crawlora:crawlora-nba:0.1.0`](java/README.md)
- PHP: [`crawlora/nba`](php/README.md)
- Rust: [`crawlora-nba`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=nba-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=nba-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=nba-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 70 selected public NBA API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/nba/box-score` | `nba-box-score` | NBA traditional box score for one game |
| `GET` | `/nba/box-score-advanced` | `nba-box-score-advanced` | NBA advanced box score for one game |
| `GET` | `/nba/box-score-defensive` | `nba-box-score-defensive` | NBA defensive box score |
| `GET` | `/nba/box-score-four-factors` | `nba-box-score-four-factors` | NBA four-factors box score for one game |
| `GET` | `/nba/box-score-misc` | `nba-box-score-misc` | NBA miscellaneous box score for one game |
| `GET` | `/nba/box-score-player-track` | `nba-box-score-player-track` | NBA player-tracking box score for one game |
| `GET` | `/nba/box-score-scoring` | `nba-box-score-scoring` | NBA scoring-distribution box score for one game |
| `GET` | `/nba/box-score-summary` | `nba-box-score-summary` | Returns the game summary tables for one game: the game summary itself plus the other summary result sets the upstream returns (line scores and officials among them) |
| `GET` | `/nba/box-score-usage` | `nba-box-score-usage` | NBA usage box score for one game |
| `GET` | `/nba/common-all-players` | `nba-common-all-players` | NBA league-wide player listing for a season |
| `GET` | `/nba/draft-combine-anthro` | `nba-draft-combine-anthro` | NBA draft combine anthropometric measurements |
| `GET` | `/nba/enums` | `nba-enums` | List the pinned NBA request enum values |
| `GET` | `/nba/franchise-history` | `nba-franchise-history` | NBA franchise history, including defunct teams |
| `GET` | `/nba/game-detail` | `nba-game-detail` | NBA game summary detail from nba.com |
| `GET` | `/nba/games` | `nba-games` | Current NBA games from nba.com's own page state |
| `GET` | `/nba/homepage-leaders` | `nba-homepage-leaders` | NBA homepage leader board |
| `GET` | `/nba/homepage-v2` | `nba-homepage-v2` | Returns the homepagev2 leader board for one stat type, scope and subject |
| `GET` | `/nba/hustle-player` | `nba-hustle-player` | Returns the league's player hustle table: contested shots, deflections, charges drawn, screen assists and points, loose balls recovered and box-outs, one row per player |
| `GET` | `/nba/hustle-stats` | `nba-hustle-stats` | NBA hustle statistics for one game |
| `GET` | `/nba/hustle-team` | `nba-hustle-team` | Returns the league's team hustle table: contested shots, deflections, charges drawn, screen assists and points, loose balls recovered and box-outs |
| `GET` | `/nba/league-game-log` | `nba-league-game-log` | NBA game log for a season, by team or by player |
| `GET` | `/nba/lineup-shot-chart` | `nba-lineup-shot-chart` | Returns the shot chart for one team's five-man lineups: one row per lineup shot with the lineup id, the game, the shooter, the period, action and shot type, the zone, distance, court coordinates and the made flag |
| `GET` | `/nba/lineups` | `nba-lineups` | NBA lineup dashboard |
| `GET` | `/nba/news` | `nba-news` | NBA news articles from nba.com |
| `GET` | `/nba/opp-pt-shot` | `nba-opp-pt-shot` | Returns the league's opponent shooting table: one row per team with the shooting it allows, split overall and from three |
| `GET` | `/nba/play-by-play` | `nba-play-by-play` | NBA play-by-play for one game |
| `GET` | `/nba/player-awards` | `nba-player-awards` | NBA player award history |
| `GET` | `/nba/player-bio-stats` | `nba-player-bio-stats` | NBA league bio table |
| `GET` | `/nba/player-career-stats` | `nba-player-career-stats` | NBA player season-by-season and career statistics |
| `GET` | `/nba/player-clutch` | `nba-player-clutch` | Returns the league's clutch player table for one clutch window and score margin: the players' clutch shooting and counting stats |
| `GET` | `/nba/player-compare` | `nba-player-compare` | NBA two-sided player comparison |
| `GET` | `/nba/player-dash-by-clutch` | `nba-player-dash-by-clutch` | Returns one player's by clutch splits as several result sets |
| `GET` | `/nba/player-dash-by-game-splits` | `nba-player-dash-by-game-splits` | Returns one player's by game splits splits as several result sets |
| `GET` | `/nba/player-dash-by-last-n-games` | `nba-player-dash-by-last-n-games` | Returns one player's by last n games splits as several result sets |
| `GET` | `/nba/player-dash-by-opponent` | `nba-player-dash-by-opponent` | Returns one player's by opponent splits as several result sets |
| `GET` | `/nba/player-dash-pt-pass` | `nba-player-dash-pt-pass` | NBA player passing dashboard |
| `GET` | `/nba/player-dash-pt-reb` | `nba-player-dash-pt-reb` | NBA player rebound dashboard |
| `GET` | `/nba/player-dash-pt-shots` | `nba-player-dash-pt-shots` | NBA player tracking shot dashboard |
| `GET` | `/nba/player-game-logs` | `nba-player-game-logs` | Returns one player's game log for a season, one row per game with the player's box-score line |
| `GET` | `/nba/player-info` | `nba-player-info` | NBA player profile |
| `GET` | `/nba/player-profile-v2` | `nba-player-profile-v2` | Returns one player's full profile stat set: the season-by-season regular-season line, the career regular-season totals and the postseason equivalents |
| `GET` | `/nba/player-pt-shot` | `nba-player-pt-shot` | Returns the league's player shooting table: one row per player with the shooting line, split overall and from three |
| `GET` | `/nba/player-stats` | `nba-player-stats` | NBA league-wide player statistics table |
| `GET` | `/nba/player-streak-finder` | `nba-player-streak-finder` | Returns player game streaks for a season: the streak rows the upstream computes, one row per streak, with the player identity and streak totals |
| `GET` | `/nba/players` | `nba-players` | NBA player index: every player id for a season |
| `GET` | `/nba/playoff-picture` | `nba-playoff-picture` | NBA playoff picture by conference |
| `GET` | `/nba/playoff-series` | `nba-playoff-series` | NBA playoff series index |
| `GET` | `/nba/pt-defend` | `nba-pt-defend` | NBA defensive tracking dashboard |
| `GET` | `/nba/pt-stats` | `nba-pt-stats` | NBA player-tracking dashboard |
| `GET` | `/nba/scoreboard` | `nba-scoreboard` | NBA scoreboard for one game day |
| `GET` | `/nba/shot-chart` | `nba-shot-chart` | NBA shot chart |
| `GET` | `/nba/standings` | `nba-standings` | NBA standings for a season and season type |
| `GET` | `/nba/synergy-play-types` | `nba-synergy-play-types` | NBA synergy play-type dashboard |
| `GET` | `/nba/team-dash-by-clutch` | `nba-team-dash-by-clutch` | Returns one team's by clutch splits as several result sets |
| `GET` | `/nba/team-dash-by-game-splits` | `nba-team-dash-by-game-splits` | Returns one team's by game splits splits as several result sets |
| `GET` | `/nba/team-dash-by-last-n-games` | `nba-team-dash-by-last-n-games` | Returns one team's by last n games splits as several result sets |
| `GET` | `/nba/team-dash-by-opponent` | `nba-team-dash-by-opponent` | Returns one team's by opponent splits as several result sets |
| `GET` | `/nba/team-dash-pt-pass` | `nba-team-dash-pt-pass` | Returns one team's passing dashboard: the pass-type breakdowns the upstream computes for that team, as several result sets |
| `GET` | `/nba/team-dash-pt-reb` | `nba-team-dash-pt-reb` | NBA team rebound dashboard |
| `GET` | `/nba/team-dash-pt-shots` | `nba-team-dash-pt-shots` | Returns one team's tracking shot dashboard: the shot breakdowns the upstream computes for that team (by touch time and shot type), as several result sets |
| `GET` | `/nba/team-details` | `nba-team-details` | NBA franchise background, season history and awards |
| `GET` | `/nba/team-game-logs` | `nba-team-game-logs` | Returns one team's game log for a season, one row per game with the team's box-score line (field goals, threes, rebounds, assists, steals, blocks, turnovers, points and plus-minus) |
| `GET` | `/nba/team-info-common` | `nba-team-info-common` | Returns one team's identity and season summary: city, name, abbreviation, code, conference and division, the win/loss record and per-game team averages, plus the team's available seasons |
| `GET` | `/nba/team-on-off` | `nba-team-on-off` | Returns a team's on-court/off-court player splits: the on-court and off-court rows the upstream computes, with each player's minutes and rating impact |
| `GET` | `/nba/team-pt-shot` | `nba-team-pt-shot` | Returns the league's team shooting table: one row per team with the shooting line, split overall and from three |
| `GET` | `/nba/team-roster` | `nba-team-roster` | NBA team roster for a season |
| `GET` | `/nba/team-shot-locations` | `nba-team-shot-locations` | NBA team shot-location dashboard |
| `GET` | `/nba/team-stats` | `nba-team-stats` | NBA league-wide team statistics table |
| `GET` | `/nba/team-stats-leaders` | `nba-team-stats-leaders` | NBA league leaders for one statistical category |
| `GET` | `/nba/team-years` | `nba-team-years` | Returns every franchise and the range of seasons it has played, one row per team |

## License

MIT. See [LICENSE](LICENSE).
