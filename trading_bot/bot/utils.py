from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from .exceptions import ValidationError


@dataclass(frozen=True)
class EnvironmentSettings:
    """Container for runtime environment configuration."""

    api_key: str
    api_secret: str
    base_url: str
    demo_mode: bool


def _is_placeholder(value: str) -> bool:
    """Return True when the provided value looks like a placeholder."""
    normalized = value.strip().lower()
    placeholder_tokens = {
        "",
        "your_api_key_here",
        "your_api_secret_here",
        "your_api_key",
        "your_api_secret",
        "changeme",
        "replace_me",
        "example",
        "placeholder",
        "demo_api_key",
        "demo_api_secret",
    }
    return normalized in placeholder_tokens or normalized.startswith("your_") or normalized.startswith("replace")


def _has_testnet_base_url(base_url: str) -> bool:
    """Validate that the configured base URL points to Binance Futures Testnet."""
    lowered = base_url.lower()
    return "testnet" in lowered and "binancefuture" in lowered


def load_environment() -> EnvironmentSettings:
    """Load configuration from the project .env file or the process environment."""
    project_root = Path(__file__).resolve().parents[2]
    env_path = project_root / ".env"
    env_file_exists = env_path.exists()
    load_dotenv(env_path)

    api_key = os.getenv("API_KEY", "").strip()
    api_secret = os.getenv("API_SECRET", "").strip()
    base_url = os.getenv("BASE_URL", "https://testnet.binancefuture.com").strip()
    demo_mode = os.getenv("DEMO_MODE", "").strip().lower() in {"1", "true", "yes", "on"}

    if not env_file_exists and not api_key and not api_secret and not demo_mode:
        raise ValidationError(
            "Configuration file .env was not found. Create one from .env.example or rerun with --demo."
        )

    if not demo_mode:
        if not _has_testnet_base_url(base_url):
            raise ValidationError("BASE_URL must point to Binance Futures Testnet in live mode.")
        if _is_placeholder(api_key) or _is_placeholder(api_secret) or not api_key or not api_secret:
            raise ValidationError(
                "Live mode requires valid API_KEY and API_SECRET values in the environment or .env file."
            )
    elif _is_placeholder(api_key) or _is_placeholder(api_secret):
        api_key = "demo_api_key"
        api_secret = "demo_api_secret"

    return EnvironmentSettings(
        api_key=api_key,
        api_secret=api_secret,
        base_url=base_url,
        demo_mode=demo_mode,
    )
