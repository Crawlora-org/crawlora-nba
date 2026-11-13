import os

from crawlora_nba import NBAClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with NBAClient(api_key=api_key) as client:
    games = client.games()
    print('games', games)
    enums = client.enums()
    print('enums', enums)
