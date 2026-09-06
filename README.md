# 🐾 QMEOW Token MCP (Model Context Protocol)

A high-performance, remote Model Context Protocol (MCP) server that exposes live price, volume, liquidity, and multi-timeframe price change percentages for `$QMEOW` (Solana). 

This server is designed to act as a public, real-time market oracle for **Claude Desktop, Cursor IDE, autonomous trading agents, and quantitative crypto bots**.

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

C. Autonomous Trading Agents & Bots (Python / Eliza Framework)
For developers running programmatic execution loops, you can connect directly to the SSE stream to fetch market telemetry on-demand:
from mcp.client.sse import sse_client
from mcp import ClientSession

async def fetch_qmeow_telemetry():
    uri = "https://qmeow-token-mcp.onrender.com/sse"
    async with sse_client(uri) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("get_token_market_data", {})
            return result.content.text

⚙️ Core Capabilities & Tools

1. get_token_market_data() [Tool]
Fetches real-time market telemetry directly from DexScreener. The response is return-trimmed on the server side to maintain a lean, low-token footprint, preventing context bloat inside your LLM agent's window.
The tool returns a highly structured JSON string specifically formatted for programmatic parsing by quantitative strategies:
Real-time Price (USD)
Multi-Timeframe price_change_percent (m5, h1, h6, h24) — crucial for momentum, breakout, trend-following, or mean-reversion trading algorithms.
24h Trading Volume (USD)
Liquidity Depth (USD)
Dex & Pair Address Metadata
Unix Fetch Timestamp

2. token://about [Resource]
Exposes a static overview of the $QMEOW token's utility as the access and computation key for the upcoming Quantum Meow hybrid AI-Quantum Orchestration Gateway (integrating local circuit simulators and IBM Partner Plus QPU runtimes).

📜 Verified Contract Mint
Solana Address: 4xYrnBTdACYetkJEAP4gj4bLFfKw9YYv1nvSWyS1pump

Always verify this contract mint address matches before executing any automated or manual trades.

🛠️ Local Development & Deployment
To run this server locally or deploy your own copy to Render:
Local Development Setup

Clone the repository: git clone <repo-url>
Install dependencies: pip install -r requirements.txt
Run the server: python qmeow_mcp_server.py (By default, running locally without a PORT environment variable will launch the server over standard input/output (stdio) for local Claude Desktop integration.)

One-Click Render Setup
Render assigns a dynamic PORT automatically. When the script detects the PORT variable on Render, it automatically binds to 0.0.0.0 and configures the sse transport layer.
Build Command: pip install -r requirements.txt
Start Command: python qmeow_mcp_server.py

## Stay tuned for MCP updates
