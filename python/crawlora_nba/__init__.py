"""Typed NBA client for the Crawlora hosted API."""

from .platform import NBAClient, AsyncNBAClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = NBAClient
AsyncClient = AsyncNBAClient
__version__ = '0.1.0'
DISPLAY_NAME = 'NBA'
PLATFORM = 'nba'
CONTRACT_REVISION = 'sha256:343b4e2ca3bea9fd723ed7fa4522b82cbfcf68cc70aec065ce0692310568d3e9'

__all__ = [
    "NBAClient", "AsyncNBAClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
