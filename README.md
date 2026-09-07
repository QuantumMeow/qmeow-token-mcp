# 🐾 QMEOW Token MCP (Model Context Protocol)

A high-performance, remote Model Context Protocol (MCP) server for crypto and quant trading bots that exposes live price, volume, liquidity, order-flow metrics, and multi-timeframe price change percentages for `$QMEOW` access token on Solana. 

This server acts as a public, real-time market oracle specifically optimized for **Claude Desktop, Cursor IDE, autonomous trading agents, and quantitative crypto bots**.

---

## 🌐 Public SSE Endpoint

* **Base URL:** `https://qmeow-token-mcp.onrender.com`
* **SSE Connection URL:** `https://qmeow-token-mcp.onrender.com/sse`
* **Transport:** Server-Sent Events (SSE)
* **Authentication:** None (Free & Public Tier)

---

## 🚀 Client Integration Configurations

### A. Claude Desktop

Add this block directly to your local configuration file:

* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "qmeow-token-oracle": {
      "url": "https://qmeow-token-mcp.onrender.com/sse",
      "transport": "sse"
    }
  }
}
```

### B. Cursor IDE

To equip your AI developer assistant with real-time token metrics, add this to your `.cursor/mcp.json` or configure it in **Settings -> MCP**:

* **Name:** `qmeow-token-oracle`
* **Type:** `SSE`
* **URL:** `https://qmeow-token-mcp.onrender.com/sse`

### C. Autonomous Trading Agents & Bots (Python / Eliza Framework)

For developers running programmatic execution loops, you can connect directly to the SSE stream to fetch market telemetry on-demand:

```python
from mcp.client.sse import sse_client
from mcp import ClientSession

async def fetch_qmeow_telemetry():
    uri = "https://qmeow-token-mcp.onrender.com/sse"
    async with sse_client(uri) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("get_token_market_data", {})
            return result.content.text
```

---

## ⚙️ Core Capabilities & Tools

### 1. `get_token_market_data()` [Tool]

Fetches real-time market telemetry directly from DexScreener. The response is return-trimmed on the server side to maintain a **lean, low-token footprint**, preventing context bloat inside your LLM agent's window. 

The tool returns a highly structured JSON string specifically formatted for programmatic parsing by quantitative strategies:

* **Real-time USD Price** (`price_usd`)
* **Real-time Native SOL Price** (`price_sol`)
* **Multi-Timeframe price_change_percent** (`m5`, `h1`, `h6`, `h24`) — *crucial for momentum, breakout, trend-following, or mean-reversion trading algorithms.*
* **Live Order Flow Metrics** (`order_flow`) — *provides exact buy/sell counts for 5m and 1h windows to gauge market velocity.*
* **Multi-Timeframe Volume breakdown** (`volume_usd` for `h1` and `h24`).
* **Liquidity Depth (USD)** (`liquidity_usd`)
* **Dex & Pair Address Metadata**
* **Unix Fetch Timestamp** (`fetched_at_unix`)

#### Example JSON Output:

```json
{
  "token": "Quantum Meow",
  "symbol": "QMEOW",
  "mint": "4xYrnBTdACYetkJEAP4gj4bLFfKw9YYv1nvSWyS1pump",
  "dex": "pump",
  "pair_address": "8X...3Y",
  "price_usd": "0.00001427",
  "price_sol": "0.0000001358",
  "price_change_percent": {
    "m5": 0.0,
    "h1": -0.5,
    "h6": 0.71,
    "h24": -3.72
  },
  "order_flow": {
    "h1": {
      "buys": 0,
      "sells": 0
    },
    "m5": {
      "buys": 0,
      "sells": 0
    }
  },
  "volume_usd": {
    "h1": 0.0,
    "h24": 429.74
  },
  "liquidity_usd": 13127.71,
  "fetched_at_unix": 1725711433
}
```

### 2. `token://about` [Resource]

Exposes a static overview of the $QMEOW token's utility as the access and computation key for the upcoming Quantum Meow hybrid AI-Quantum Orchestration Gateway.

---

## 📜 Verified Contract Mint

* **Solana Address:** `4xYrnBTdACYetkJEAP4gj4bLFfKw9YYv1nvSWyS1pump`
  
  > *Always verify this contract mint address matches before executing any automated or manual trades.*

---

## 🛠️ Local Development & Deployment

To run this server locally or deploy your own copy to Render:

### Local Development Setup

1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python qmeow_mcp_server.py`
   *(By default, running locally without a `PORT` environment variable will launch the server over standard input/output (`stdio`) for local Claude Desktop integration.)*

### One-Click Render Setup

Render assigns a dynamic `PORT` automatically. When the script detects the `PORT` variable on Render, it automatically binds to `0.0.0.0` and configures the `sse` transport layer.

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `python qmeow_mcp_server.py`
