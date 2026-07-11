# 🚀 Binance Futures Testnet Trading Bot (CLI)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)
![Status](https://img.shields.io/badge/Status-Internship%20Project-success.svg)
![Platform](https://img.shields.io/badge/Platform-CLI-orange.svg)

A production-style **Python Command Line Interface (CLI)** application for placing **BUY** and **SELL** orders on the **Binance USDT-M Futures Testnet**. The project demonstrates clean backend architecture, modular design, secure credential management, robust input validation, structured logging, and professional exception handling.

To support evaluation without requiring Binance credentials, the application includes a **Demo Mode** that simulates realistic Binance API responses while preserving the same workflow as Live Mode.

---

# ✨ Key Features

| Feature | Status |
|----------|--------|
| MARKET Orders | ✅ |
| LIMIT Orders | ✅ |
| BUY / SELL Support | ✅ |
| Binance Futures Testnet Integration | ✅ |
| Demo Mode | ✅ |
| Rich CLI Interface | ✅ |
| Secure Environment Variables | ✅ |
| Input Validation | ✅ |
| Professional Logging | ✅ |
| Exception Handling | ✅ |
| Modular Architecture | ✅ |

---

# 🏗 System Architecture

```text
                    +----------------------+
                    |      CLI (main.py)   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Argument Parsing     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Input Validation     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Environment Loader   |
                    | (.env Configuration) |
                    +----------+-----------+
                               |
                               v
               +-------------------------------+
               | Trading Client                |
               |-------------------------------|
               | Live Binance Client           |
               | OR                            |
               | Demo Trading Client           |
               +---------------+---------------+
                               |
                               v
                    +----------------------+
                    | Logging & Console    |
                    +----------------------+
```

---

# ⚙ Execution Flow

```text
CLI
 │
 ▼
Argument Parsing
 │
 ▼
Input Validation
 │
 ▼
Environment Configuration
 │
 ▼
Trading Client
 │
 ├── Live Mode
 │      │
 │      ▼
 │ Binance Futures Testnet
 │
 └── Demo Mode
        │
        ▼
 Mock Binance Response
 │
 ▼
Logging
 │
 ▼
Console Output
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Core Programming Language |
| python-binance | Binance Futures API Integration |
| argparse | Command Line Interface |
| Rich | Enhanced Terminal Output |
| python-dotenv | Environment Variable Management |
| logging | Structured Logging |
| requests | HTTP Communication |
| pytest | Unit Testing |

---

# 📂 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── exceptions.py
│   └── utils.py
│
├── logs/
│   └── trading_bot.log
│
├── tests/
│
├── .env.example
├── LICENSE
├── README.md
├── requirements.txt
└── main.py
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/binance-futures-testnet-trading-bot.git
cd binance-futures-testnet-trading-bot
```

## 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuration

Create a `.env` file using `.env.example`.

```env
API_KEY=**************
API_SECRET=************
BASE_URL=https://testnet.binancefuture.com
DEMO_MODE=false
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| API_KEY | Binance Futures Testnet API Key |
| API_SECRET | Binance Futures Testnet Secret Key |
| BASE_URL | Binance Futures Testnet Endpoint |
| DEMO_MODE | Enables simulated order execution |

---

# 💻 Usage

## ▶ Live Mode

Requires valid Binance Futures Testnet credentials.

Market Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Limit Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 120000
```

---

## ▶ Demo Mode

Runs without Binance credentials.

```bash
python main.py --demo --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

> **Note**
>
> Demo Mode generates deterministic Binance-style responses for development, testing, and project evaluation. No requests are sent to Binance while running in Demo Mode.

---

# 📷 Sample Output

```text
========================================
 Binance Futures Trading Bot
========================================

Execution Mode : DEMO

----------------------------------------
Order Summary
----------------------------------------

Symbol        : BTCUSDT
Side          : BUY
Order Type    : MARKET
Quantity      : 0.01
Price         : MARKET

----------------------------------------

API Response

Order ID            : demo-BTCUSDT-buy
Status              : FILLED
Executed Quantity   : 0.01
Average Price       : 100000.0
Client Order ID     : demo-client-BTCUSDT-buy

Demo Mode: Simulated order executed successfully.
No request was sent to the Binance Futures Testnet.
```

---

# 📸 Screenshots
<img width="1281" height="629" alt="Screenshot 2026-07-11 180259" src="https://github.com/user-attachments/assets/57d64c6b-703f-4979-9c92-edad3034d42e" />

---

# 📝 Logging

Application logs are automatically stored in:

```text
logs/trading_bot.log
```

Each execution records:

- Timestamp
- Execution Mode
- Order Parameters
- API Requests
- API Responses
- Execution Time
- Warnings
- Errors
- Exceptions

Example

```text
2026-07-11 17:53:41 INFO

Execution Mode : DEMO

Order

Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.01

Result

Status : FILLED
OrderID: demo-BTCUSDT-buy
Execution Time : 0.001s
```

---

# ⚠ Error Handling

The application gracefully handles:

| Error Type | Description |
|------------|-------------|
| Authentication Errors | Invalid API credentials |
| Validation Errors | Invalid CLI arguments |
| Network Errors | Internet connectivity issues |
| Timeout Errors | API request timeout |
| Rate Limiting | Binance API restrictions |
| Environment Errors | Missing or invalid configuration |
| Unexpected Exceptions | Graceful fallback with meaningful messages |

Raw Python tracebacks are never shown to end users.

---

# 🔒 Security

- API credentials are stored securely using environment variables.
- API secrets are never printed or logged.
- Sensitive information is masked where applicable.
- Configuration is validated before execution.
- Demo Mode prevents accidental live order execution.

---

# 📌 Design Decisions

This project follows a modular backend architecture with clear separation of concerns.

- Dedicated validation layer
- Centralized logging configuration
- Client abstraction for Live and Demo execution
- Reusable order models
- Externalized configuration
- Clean exception hierarchy

The design emphasizes readability, maintainability, and extensibility.

---

# ⚠ Known Limitations

- Demo Mode simulates Binance responses and does not place real orders.
- Live Mode requires valid Binance Futures Testnet credentials.
- Binance API permissions, account configuration, or IP restrictions may prevent live order execution.
- The application currently supports MARKET and LIMIT orders only.

---

# 🚀 Future Improvements

- [ ] Stop-Loss Orders
- [ ] Take-Profit Orders
- [ ] OCO Orders
- [ ] Docker Support
- [ ] GitHub Actions CI/CD
- [ ] Asynchronous API Requests
- [ ] Portfolio Dashboard
- [ ] Trading History Export
- [ ] Enhanced Retry Mechanism

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

# 📜 License

This project is licensed under the **Apache License 2.0**.

See the **LICENSE** file for complete license information.

---

# 👨‍💻 Author

**G. Manohara**

---

# 🎯 Project Objective

This project was developed as part of a **Python Backend Internship Assignment** to demonstrate practical knowledge of:

- Python Backend Development
- REST API Integration
- Command-Line Application Development
- Secure Credential Management
- Software Architecture & Design
- Logging & Exception Handling
- Clean Code Principles
- Professional Project Documentation

The project emphasizes writing maintainable, production-oriented Python code while following software engineering best practices.
