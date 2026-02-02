# Binance Futures Testnet Trading Bot (Python)

## Overview

This project is a simplified Python trading bot built for the **Binance Futures Testnet (USDT-M)**.  
It allows placing **MARKET**, **LIMIT**, and **STOP-LIMIT** orders using a **CLI interface**, with proper **logging**, **validation**, and **error handling**.


---

## Features

- Binance **Futures Testnet (USDT-M)** integration
- Place orders:
  - MARKET
  - LIMIT
  - STOP-LIMIT (Bonus)
- Supports both **BUY** and **SELL**
- Command-line interface using `argparse`
- Input validation
- Structured logging
- Exception handling for API and exchange errors

---

## Project Structure
``` bash
trading_bot/
├── bot/
│ ├── init.py
│ ├── client.py # Binance Futures client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ └── logging_config.py # Logging configuration
│
├── cli.py # CLI entry point
├── logs/
│ ├── market_order.log
│ ├── limit_order.log
│ └── stop_limit_order.log
│
├── requirements.txt
├── README.md
└── .env # API keys (not committed)
``` 
---
## Setup Instructions (macOS)

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd trading_bot
```
### 2. Create and activate virtual environment
``` bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
``` bash
pip install -r requirements.txt
```
### 4. Configure environment variables
Create a .env file in the project root:
``` bash
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

### Binance Futures Testnet

- Base URL used by the application:
``` bash
https://testnet.binancefuture.com
```

 - Testnet funds are added via the demo UI using Get Testnet USDT
 - No real money is involved


## How to Run

Make sure the virtual environment is activated.

 - MARKET Order (BUY)
 ``` bash
python3 cli.py \
  --symbol BTCUSDT \
  --side BUY \
  --type MARKET \
  --quantity 0.003
  ```

- LIMIT Order (SELL)
``` bash
python3 cli.py \
  --symbol BTCUSDT \
  --side SELL \
  --type LIMIT \
  --quantity 0.003 \
  --price 90000
```
- STOP-LIMIT Order (Bonus)
``` bash
python3 cli.py \
  --symbol BTCUSDT \
  --side SELL \
  --type STOP_LIMIT \
  --quantity 0.003 \
  --stop_price 44000 \
  --price 43000
  ```


## CLI Output:

- Each command prints:

- Place orders:
  - Order ID
  - Status
  - Executed quantity
  - Average price (if available)
- Success or error message

## Logging
All API requests, responses, and errors are logged to files.

#### Example log entry:
``` bash
2026-02-02 10:55:39 | INFO | Request: BTCUSDT BUY MARKET qty=0.003
2026-02-02 10:55:39 | INFO | Response: {...}
```
#### Included Log Files

 - logs/market_order.log

 - logs/limit_order.log

 - logs/stop_limit_order.log

## Error Handling

#### The application handles:

 - Invalid CLI inputs

 - Missing or incorrect API credentials

 - Binance API errors

 - Exchange rule violations (e.g., minimum notional value, immediate trigger)


#### Errors are both:

- Displayed in the CLI

- Logged with timestamps

## Assumptions & Notes
- Binance Futures Testnet may return:

  - NEW status for MARKET orders
  - Partial or minimal responses for STOP-LIMIT orders
 - This is expected behavior in the simulated environment.

 - The project focuses on API integration and application structure, not trading strategies.

 - No real funds are used.
