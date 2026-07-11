# 🚀 Binance Futures Testnet Trading Bot (CLI)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Internship%20Project-success.svg)
![Platform](https://img.shields.io/badge/Platform-CLI-orange.svg)

A production-ready **Python Command Line Interface (CLI)** application for executing **BUY** and **SELL** orders on the **Binance Futures Testnet**. The project emphasizes clean architecture, secure credential management, modular design, comprehensive logging, robust input validation, and professional error handling.

The application supports both **Live Mode** (Binance Futures Testnet) and **Demo Mode**, allowing recruiters and developers to evaluate the application without requiring live API credentials.

---

# ✨ Key Features

| Feature | Status |
|----------|--------|
| MARKET Orders | ✅ |
| LIMIT Orders | ✅ |
| BUY / SELL Support | ✅ |
| Binance Futures Testnet Integration | ✅ |
| Demo Mode | ✅ |
| Secure Environment Variables | ✅ |
| CLI Interface | ✅ |
| Rich Terminal Output | ✅ |
| Input Validation | ✅ |
| Professional Logging | ✅ |
| Exception Handling | ✅ |
| Modular Architecture | ✅ |

---

# 🏗 Architecture

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
 │  Binance Futures Testnet
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
| python-binance | Binance API Integration |
| argparse | Command Line Interface |
| Rich | Professional Terminal Output |
| python-dotenv | Environment Variable Management |
| logging | Application Logging |
| requests | HTTP Requests |
| pytest | Unit Testing |

---

# 📁 Project Structure

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
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---

# 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuration

Create a `.env` file.

```env
API_KEY=
API_SECRET=
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

## Live Mode

Uses Binance Futures Testnet credentials.

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Limit Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 120000
```

---

## Demo Mode

Runs without Binance credentials.

```bash
python main.py --demo --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Demo Mode returns deterministic Binance-style responses and is intended for development, testing, and project evaluation.

---

# 🖥 Sample Output

```text
========================================
 Binance Futures Trading Bot
========================================

Execution Mode : DEMO

------------------------------------
Order Summary
------------------------------------

Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.01

------------------------------------

Order ID            : demo-order-id
Status              : MOCKED
Executed Quantity   : 0.01
Average Price       : 0.0
Client Order ID     : demo-client-order-id

✓ Order placed successfully
```

---

# 📸 Screenshots

> Replace these placeholders with screenshots of your application.

- CLI Execution
- Demo Mode Output
- Live Mode Output
- Logging Output

---

# 📄 Logging

Logs are automatically written to:

```text
logs/trading_bot.log
```

Each log records:

- Timestamp
- Execution Mode
- Order Parameters
- API Request
- API Response
- Warnings
- Errors
- Exceptions

Example

```text
2026-07-11 16:51:05 INFO

Execution Mode : DEMO

Order

Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.01

Result

Status : MOCKED
OrderID: demo-order-id
```

---

# ⚠ Error Handling

| Error | Description |
|--------|-------------|
| Authentication Error | Invalid API credentials |
| Network Error | Internet connectivity issues |
| Timeout | API request timeout |
| Validation Error | Invalid CLI arguments |
| Environment Error | Missing configuration |
| Rate Limit Error | Binance API rate limit exceeded |
| Unexpected Error | Gracefully handled runtime exceptions |

---

# 🔒 Security

- API credentials are stored securely using environment variables.
- API secrets are never logged or printed.
- Sensitive values are masked where applicable.
- Demo Mode prevents accidental live order execution.
- Configuration is validated before execution.

---

# 📌 Design Decisions

The project follows a modular architecture with clear separation of concerns.

- Validation is isolated from business logic.
- Logging is centralized.
- Trading operations are encapsulated.
- Environment configuration is externalized.
- Demo Mode enables safe evaluation without live credentials.

---

# ⚠ Known Limitations

- Demo Mode simulates Binance responses and does not place real orders.
- Live Mode requires valid Binance Futures Testnet credentials.
- Binance API permissions or IP restrictions may prevent order execution.
- The application currently supports MARKET and LIMIT orders only.

---

# 🚀 Future Improvements

- [ ] Stop-Loss Orders
- [ ] Take-Profit Orders
- [ ] Docker Support
- [ ] GitHub Actions CI/CD
- [ ] Advanced Unit Tests
- [ ] Retry Mechanism
- [ ] Async API Requests
- [ ] Portfolio Dashboard
- [ ] Order History Export

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

# 📜 License

This project is released under the **MIT License**.

---

# 👨‍💻 Author

**G. Manohara**

Computer Science & Business Systems (CSBS) Student  
Python Backend Developer | Web Developer | AI Enthusiast

---

## ⭐ Project Purpose

This project was developed as a **Python Backend Internship Assignment** to demonstrate practical skills in:

- REST API Integration
- Python Backend Development
- CLI Application Development
- Secure Credential Management
- Software Architecture
- Logging & Exception Handling
- Clean Code Practices
- Professional Project Documentation
