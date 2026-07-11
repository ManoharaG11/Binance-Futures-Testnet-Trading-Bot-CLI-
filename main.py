from __future__ import annotations

import argparse
import sys
from typing import Sequence

from rich.console import Console
from rich.panel import Panel

from trading_bot.bot.client import BinanceFuturesClient
from trading_bot.bot.exceptions import AuthenticationError, RateLimitError, TradingBotError, ValidationError
from trading_bot.bot.logging_config import setup_logging
from trading_bot.bot.orders import render_order_summary
from trading_bot.bot.utils import EnvironmentSettings, load_environment
from trading_bot.bot.validators import build_order_request


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(description="Place BUY/SELL orders on Binance Futures Testnet")
    parser.add_argument("--symbol", required=True, help="Trading symbol, for example BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price (required for LIMIT orders)")
    parser.add_argument("--demo", action="store_true", help="Run in demo mode without sending real Binance requests")
    return parser


def _render_banner(console: Console, execution_mode: str) -> None:
    """Render a polished banner for the CLI."""
    console.print()
    console.print(
        Panel.fit(
            f"[bold cyan]Binance Trading Bot[/bold cyan]\n\nExecution Mode: [bold]{execution_mode}[/bold]",
            border_style="cyan",
            title="[bold]Binance Futures Testnet[/bold]",
        )
    )


def _render_response(console: Console, result: dict[str, object]) -> None:
    """Render the order response in a readable format."""
    console.print("[bold green]API Response[/bold green]")
    console.print(f"Order ID: {result['order_id']}")
    console.print(f"Status: {result['status']}")
    console.print(f"Executed Quantity: {result['executed_quantity']}")
    console.print(f"Average Price: {result['average_price']}")
    console.print(f"Client Order ID: {result['client_order_id']}")


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the CLI application."""
    parser = build_parser()
    args = parser.parse_args(argv)
    logger = setup_logging()
    console = Console()

    try:
        order_request = build_order_request(args)
        env_settings: EnvironmentSettings = load_environment()
        execution_mode = "DEMO" if args.demo or env_settings.demo_mode else "LIVE"

        _render_banner(console, execution_mode)
        logger.info("Starting %s order placement workflow", execution_mode)
        render_order_summary(order_request, console, execution_mode)

        client = BinanceFuturesClient(
            api_key=env_settings.api_key,
            api_secret=env_settings.api_secret,
            base_url=env_settings.base_url,
            logger=logger,
            demo_mode=args.demo or env_settings.demo_mode,
        )

        result = client.place_order(order_request)
        _render_response(console, result)

        if execution_mode == "DEMO":
            console.print("[yellow]⚠ Demo mode enabled; no real Binance order was sent.[/yellow]")
        else:
            console.print("[green]✓ Order placed successfully[/green]")
        logger.info("Order completed successfully in %s mode", execution_mode)
        return 0
    except ValidationError as exc:
        logger.error("Validation failed: %s", exc)
        console.print(f"[red]✗ {exc}[/red]")
        return 2
    except AuthenticationError as exc:
        logger.error("Authentication failed: %s", exc)
        console.print("[red]✗ Authentication failed. Please verify your credentials or rerun with --demo.[/red]")
        return 1
    except RateLimitError as exc:
        logger.error("Rate limit reached: %s", exc)
        console.print("[yellow]⚠ Binance rate limit reached. Please wait and retry.[/yellow]")
        return 1
    except TradingBotError as exc:
        logger.error("Trading bot error: %s", exc)
        console.print(f"[red]✗ {exc}[/red]")
        return 1
    except KeyboardInterrupt:
        logger.warning("Execution interrupted by user")
        console.print("[yellow]✗ Operation cancelled by user[/yellow]")
        return 130
    except Exception as exc:  # pragma: no cover - defensive fallback
        logger.exception("Unexpected exception: %s", exc)
        console.print("[red]✗ Unexpected error. Please review the logs and try again.[/red]")
        return 1


if __name__ == "__main__":
    sys.exit(main())
