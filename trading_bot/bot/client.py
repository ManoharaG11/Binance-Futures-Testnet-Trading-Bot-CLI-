from __future__ import annotations

import time
from typing import Any

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from requests.exceptions import RequestException, Timeout

from .exceptions import ApiError, AuthenticationError, NetworkError, RateLimitError, TradingBotError
from .logging_config import setup_logging
from .validators import OrderRequest


class BinanceFuturesClient:
    """Wrapper for Binance Futures Testnet order placement."""

    def __init__(self, api_key: str, api_secret: str, base_url: str, logger: Any | None = None, demo_mode: bool = False) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.logger = logger or setup_logging()
        self.demo_mode = demo_mode
        self.client = None if demo_mode else Client(api_key=api_key, api_secret=api_secret, testnet=True)

    def place_order(self, order_request: OrderRequest) -> dict[str, Any]:
        """Send a market or limit order to Binance Futures Testnet."""
        started_at = time.perf_counter()
        request_mode = "DEMO" if self.demo_mode else "LIVE"
        self.logger.info(
            "%s ORDER | Symbol: %s | Side: %s | Type: %s | Quantity: %s | Price: %s",
            request_mode,
            order_request.symbol,
            order_request.side,
            order_request.order_type,
            order_request.quantity,
            order_request.price if order_request.price is not None else "MARKET",
        )

        if self.demo_mode:
            self.logger.warning("Demo mode enabled; skipping real Binance request")
            response = self._build_demo_response(order_request)
            self.logger.info("Demo response: %s", response)
            self._log_execution_time(started_at)
            return self._normalize_response(response)

        params = self._build_live_params(order_request)
        self.logger.info("Live request payload: %s", params)

        try:
            response = self.client.futures_create_order(**params)
            self.logger.info("Live response: %s", response)
            self._log_execution_time(started_at)
            return self._normalize_response(response)
        except BinanceAPIException as exc:
            self.logger.error("Binance API error: %s", exc)
            if getattr(exc, "status_code", None) in {401, 403}:
                raise AuthenticationError("Binance authentication failed. Check API_KEY and API_SECRET.") from exc
            if getattr(exc, "status_code", None) == 429:
                raise RateLimitError("Binance rate limit reached. Please retry shortly.") from exc
            raise ApiError(f"Binance API error: {exc}") from exc
        except Timeout as exc:
            self.logger.error("Request timed out: %s", exc)
            raise NetworkError("The Binance request timed out. Please retry.") from exc
        except RequestException as exc:
            self.logger.error("Network error: %s", exc)
            raise NetworkError(f"Network request failed: {exc}") from exc
        except AuthenticationError as exc:
            self.logger.error("Authentication error: %s", exc)
            raise
        except Exception as exc:  # pragma: no cover - defensive fallback
            self.logger.exception("Unexpected error while placing order: %s", exc)
            raise TradingBotError(f"Unexpected error: {exc}") from exc

    def _build_live_params(self, order_request: OrderRequest) -> dict[str, Any]:
        """Build the payload for a Binance Futures order request."""
        params: dict[str, Any] = {
            "symbol": order_request.symbol,
            "side": order_request.side,
            "type": order_request.order_type,
            "quantity": order_request.quantity,
        }
        if order_request.order_type == "LIMIT" and order_request.price is not None:
            params["price"] = order_request.price
        return params

    def _build_demo_response(self, order_request: OrderRequest) -> dict[str, Any]:
        """Return a deterministic Binance-like response for demo mode."""
        return {
            "symbol": order_request.symbol,
            "side": order_request.side,
            "type": order_request.order_type,
            "orderId": f"demo-{order_request.symbol}-{order_request.side.lower()}",
            "status": "FILLED",
            "executedQty": str(order_request.quantity),
            "avgPrice": str(order_request.price or 100000.0),
            "clientOrderId": f"demo-client-{order_request.symbol}-{order_request.side.lower()}",
            "origQty": str(order_request.quantity),
            "price": str(order_request.price or 100000.0),
        }

    def _normalize_response(self, response: dict[str, Any]) -> dict[str, Any]:
        """Normalize Binance responses for consistent output."""
        return {
            "order_id": response.get("orderId", "N/A"),
            "status": response.get("status", "UNKNOWN"),
            "executed_quantity": response.get("executedQty", "0"),
            "average_price": response.get("avgPrice", "0"),
            "client_order_id": response.get("clientOrderId", "N/A"),
        }

    def _log_execution_time(self, started_at: float) -> None:
        """Log the time taken to complete the request."""
        elapsed = time.perf_counter() - started_at
        self.logger.info("Execution time: %.3fs", elapsed)
