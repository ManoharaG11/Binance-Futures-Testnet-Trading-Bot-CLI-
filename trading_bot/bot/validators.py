from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Sequence

from .exceptions import ValidationError


@dataclass(frozen=True)
class OrderRequest:
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: float | None = None


def _ensure_finite_number(value: float, field_name: str) -> float:
    """Ensure explicit numeric values are finite and not negative or zero."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValidationError(f"{field_name} must be a numeric value.")
    if not math.isfinite(float(value)):
        raise ValidationError(f"{field_name} must be a finite number.")
    return float(value)


def validate_symbol(symbol: str) -> str:
    """Validate the trading symbol format."""
    if not isinstance(symbol, str):
        raise ValidationError("Symbol is required.")
    normalized_symbol = symbol.strip()
    if not normalized_symbol:
        raise ValidationError("Symbol is required.")
    if normalized_symbol != normalized_symbol.upper():
        raise ValidationError("Symbol must be uppercase, e.g. BTCUSDT.")
    if not normalized_symbol.endswith("USDT"):
        raise ValidationError("Only USDT-margined futures symbols are supported in this assignment.")
    return normalized_symbol


def validate_side(side: str) -> str:
    """Validate the order side."""
    normalized_side = side.strip().upper()
    if normalized_side not in {"BUY", "SELL"}:
        raise ValidationError("Side must be either BUY or SELL.")
    return normalized_side


def validate_order_type(order_type: str) -> str:
    """Validate the order type."""
    normalized_type = order_type.strip().upper()
    if normalized_type not in {"MARKET", "LIMIT"}:
        raise ValidationError("Type must be either MARKET or LIMIT.")
    return normalized_type


def validate_quantity(quantity: float) -> float:
    """Validate the order quantity."""
    numeric_quantity = _ensure_finite_number(quantity, "Quantity")
    if numeric_quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")
    return numeric_quantity


def validate_price(price: float | None, order_type: str) -> float | None:
    """Validate the price for LIMIT orders."""
    if order_type == "LIMIT":
        if price is None:
            raise ValidationError("Price is required for LIMIT orders.")
        numeric_price = _ensure_finite_number(price, "Price")
        if numeric_price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return numeric_price
    return None


def build_order_request(args: argparse.Namespace) -> OrderRequest:
    """Build and validate a normalized order request from CLI arguments."""
    symbol = validate_symbol(getattr(args, "symbol", ""))
    side = validate_side(getattr(args, "side", ""))
    order_type = validate_order_type(getattr(args, "type", ""))
    quantity = validate_quantity(getattr(args, "quantity", 0))
    price = validate_price(getattr(args, "price", None), order_type)

    return OrderRequest(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Compatibility helper for CLI argument parsing."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)
    return parser.parse_args(argv)
