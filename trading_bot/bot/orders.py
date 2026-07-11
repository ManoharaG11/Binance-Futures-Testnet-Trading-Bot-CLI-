from __future__ import annotations

from typing import Any

from rich.console import Console

from .validators import OrderRequest, build_order_request as build_validated_request


def build_order_request(args: Any) -> OrderRequest:
    """Create and validate an order request object from CLI arguments."""
    return build_validated_request(args)


def render_order_summary(order_request: OrderRequest, console: Console, execution_mode: str) -> None:
    """Render a readable order summary before placing the order."""
    console.print()
    console.print("[bold cyan]Order Summary[/bold cyan]")
    console.print("[cyan]" + "-" * 36 + "[/cyan]")
    console.print(f"Execution Mode: [bold]{execution_mode}[/bold]")
    console.print(f"Symbol: {order_request.symbol}")
    console.print(f"Side: {order_request.side}")
    console.print(f"Order Type: {order_request.order_type}")
    console.print(f"Quantity: {order_request.quantity}")
    console.print(f"Price: {order_request.price if order_request.price is not None else 'MARKET'}")
    console.print("[cyan]" + "-" * 36 + "[/cyan]")
    console.print()
