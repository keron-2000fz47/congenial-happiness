# 🤖 PumpFun Trading Bot

> A powerful Solana trading & token sniping bot for [pump.fun](https://pump.fun), written in Python.

---

**⚠️ NOT FOR PRODUCTION**: This code is for educational and research purposes only. Use at your own risk. The authors assume no responsibility for any financial losses.

**🚨 SCAM ALERT**: Be cautious of any third-party links shared in Issues. Never share your private key with anyone.

---

## ✨ Features

- 🎯 **Token Sniping** — snipe newly launched tokens on pump.fun the moment they appear
- 📈 **Take Profit / Stop Loss** — automated exit strategies to secure gains or limit losses
- 🔄 **Dual Subscription** — supports both `logsSubscribe` and `blockSubscribe` for flexibility
- ⚡ **Geyser / gRPC Streaming** — real-time data via Yellowstone gRPC (Jito ShredStream enabled by default)
- 🏗️ **Token Minting** — ability to mint tokens on pump.fun
- 🔁 **Auto Retry Logic** — exponential backoff on 429 / RPC errors
- 🪣 **Token Bucket Rate Limiter** — built-in RPC rate limiting (default 25 RPS)
- 📊 **Bonding Curve Tracking** — monitor bonding curve progress and predict migration timing
- 🔀 **PumpSwap Migration Listener** — listens to token graduation events from bonding curves to PumpSwap AMM
- ⚙️ **YAML-based Bot Config** — each `.yaml` file in `bots/` is an independent bot instance

---

## 🚀 Getting Started

### Prerequisites

- Install [uv](https://github.com/astral-sh/uv) — a fast Python package manager.

> If Python is already installed, `uv` will detect and use it automatically.

### Installation

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/keron-2000fz47/congenial-happiness.git
cd congenial-happiness
```

#### 2️⃣ Set up a virtual environment
```bash
uv sync

# Activate (Unix/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

#### 3️⃣ Configure the bot
```bash
cp .env.example .env       # Unix/macOS
copy .env.example .env     # Windows
```

Edit `.env` and add your **Solana RPC endpoint** and **wallet private key**.

Edit `.yaml` templates in `bots/` — each file is a separate bot instance. Set `platform: "pump_fun"` to trade on pump.fun.

#### 4️⃣ Install as a package
```bash
uv pip install -e .
```

### Running the Bot

```bash
# Option 1: run as installed package
pump_bot

# Option 2: run directly
uv run src/bot_runner.py
```

> **You're all set! 🎉**

---

## ⚙️ Configuration

| Parameter | Description |
|-----------|-------------|
| `platform` | `pump_fun` |
| `max_rps` | Maximum RPC requests per second (default: 25) |
| `take_profit` | Target profit percentage to sell |
| `stop_loss` | Max loss percentage before auto-sell |
| `subscription_method` | `logs` or `block` subscribe |

---

## 🗺️ Roadmap

| Feature | Status |
|---------|--------|
| Token sniping via `logsSubscribe` | ✅ |
| Token sniping via `blockSubscribe` | ✅ |
| Take profit / Stop loss | ✅ |
| Geyser / gRPC streaming | ✅ |
| Token minting | ✅ |
| Dynamic priority fees | ✅ |
| Configurable RPS limiter | ✅ |
| Bonding curve status tracking | ✅ |
| PumpSwap migration listener | ✅ |
| Market cap-based selling | 🔜 |
| Copy trading | 🔜 |
| Token analysis (market cap, liquidity, age) | 🔜 |

---

## 📁 Project Structure

```
congenial-happiness/
├── bots/               # YAML bot configuration files
├── src/                # Core bot source code
├── idl/                # Solana program IDL files
├── learning-examples/  # Standalone scripts & examples
│   ├── listen-new-tokens/
│   ├── listen-migrations/
│   └── bonding-curve-progress/
├── trades/             # Trade logs
├── landing/            # Landing page (GitHub Pages)
├── .env.example        # Environment variable template
└── pyproject.toml      # Project dependencies
```

---

## ⚠️ RPC & Rate Limiting

Public RPC nodes will not work for heavy sniping. You need a dedicated Solana RPC endpoint.

The bot includes a built-in **token bucket rate limiter**:
- Smoothly controls request rate with burst support
- Configurable `max_rps` per `SolanaClient`
- Auto-retry with exponential backoff on `429` errors
- Shared session for connection reuse

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.