from __future__ import annotations


class TradingBotError(Exception):
    """Base class for trading bot errors."""


class ValidationError(TradingBotError):
    """Raised when CLI or order validation fails."""


class AuthenticationError(TradingBotError):
    """Raised when Binance authentication fails."""


class ApiError(TradingBotError):
    """Raised when Binance returns an API error."""


class NetworkError(TradingBotError):
    """Raised when the network request fails."""


class RateLimitError(TradingBotError):
    """Raised when Binance rate limits the request."""
