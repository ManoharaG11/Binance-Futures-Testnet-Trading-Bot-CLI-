# Binance Futures Testnet Trading Bot (CLI)

## Project Overview
This CLI application provides a clean, modular interface for submitting BUY and SELL orders to Binance Futures Testnet. It supports both Live Mode and Demo Mode and is structured for maintainability, clear logging, and interview-ready code quality.

## Architecture Diagram
```text
+-------------------+
|  CLI / argparse   |
+---------+---------+
          |
          v
+-------------------+
|  Order Validation |
+-------------------+
          |
          v
+-------------------+
|  Environment      |
|  Loader (.env)    |
+-------------------+
          |
          v
+-------------------+
|  Binance Client   |
|  (Live or Demo)   |
+-------------------+
          |
          v
+-------------------+
|  Rich Console     |
|  + Logging        |
+-------------------+
```

## Features
- Place MARKET and LIMIT orders
- Support BUY and SELL orders
- Use Binance Futures Testnet in Live Mode
- Run safely in Demo Mode without API keys
- Validate CLI inputs and order parameters
- Log requests, responses, warnings, and failures
- Display rich terminal output with a professional banner

## Folder Structure
```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── exceptions.py
│   └── utils.py
├── logs/
│   └── trading_bot.log
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

## Installation
1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the environment template and adjust it:

```bash
copy .env.example .env
```

## Requirements
- Python 3.11+
- python-binance
- python-dotenv
- rich
- requests
- pytest

## Environment Variables
Create a .env file from .env.example:

```env
API_KEY=
API_SECRET=
BASE_URL=https://testnet.binancefuture.com
DEMO_MODE=false
```

## Demo Mode
Demo Mode allows recruiters or reviewers to run the CLI without real Binance credentials. It returns deterministic Binance-style responses and is intended for safe local verification.

```bash
python main.py --demo --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

## Live Mode
Live Mode uses real Binance Futures Testnet credentials.

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

## Sample Outputs
```text
==============================
Binance Trading Bot
==============================
Execution Mode: DEMO

Order Summary
...

API Response
Order ID: demo-order-id
Status: MOCKED
```

## Screenshots
Screenshots can be added here once the project is demonstrated in a terminal or during a live review session.

## How Logging Works
Logs are written to logs/trading_bot.log and also printed to the console. Each entry records the timestamp, execution mode, order details, response data, warnings, and errors.

## Error Handling
The bot handles:
- Invalid CLI input
- Invalid symbols
- Invalid quantity and price values
- Missing or invalid environment settings
- Binance authentication failures
- Network and timeout issues
- Rate limiting
- Unexpected exceptions
- Non-finite numeric input such as NaN or Infinity

## Security Notes
- API secrets are never printed to the terminal.
- The code validates configuration before startup.
- Demo Mode avoids accidental live trading with placeholder credentials.

## Known Limitations
- Demo Mode simulates responses and does not place real orders.
- Actual order placement requires valid Binance Futures Testnet credentials.
- Binance API permissions and IP restrictions may still block a request even when the credentials are syntactically valid.

## Future Improvements
- Add retry logic for transient request failures
- Add stop-loss and take-profit order support
- Add integration tests for live API flows using mocks
- Add richer progress indicators and command presets

## Developer Notes
- The architecture is intentionally modular and small.
- Core concerns are separated into validation, order creation, client execution, and logging.

## License
This project is intended for educational and internship demonstration purposes.
