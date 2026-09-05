# QMEOW Token MCP

A remote MCP (Model Context Protocol) server that exposes live price,
volume, and liquidity data for $QMEOW (Solana) via DexScreener, for use
with Claude Desktop, Claude.ai, and other MCP-compatible clients.

## Setup (local development)

```bash
pip install -r requirements.txt
python qmeow_mcp_server.py
```

The server runs on Streamable HTTP, binding to `0.0.0.0` and reading
`PORT` from the environment (defaults to 8000 locally).

## Deploying to Render

This repo includes a `render.yaml` for one-click infrastructure setup.
In the Render dashboard:

1. New → Web Service → connect this repo
2. Build command: `pip install -r requirements.txt`
3. Start command: `python qmeow_mcp_server.py`
4. Render assigns `PORT` automatically — no manual config needed

Once deployed, connect it in Claude Desktop or Claude.ai via
**Settings → Connectors → Add custom connector**, using your Render
service's public URL (e.g. `https://qmeow-token-mcp.onrender.com/mcp`).

## What it does

- `get_token_market_data()` — returns current price, 24h volume, and
  liquidity for $QMEOW as JSON, sourced from DexScreener
- `token://about` — a short project overview resource

## Contract address

`4xYrnBTdACYetkJEAP4gj4bLFfKw9YYv1nvSWyS1pump` — always verify this
matches before trusting any $QMEOW price data.

## Status

Early stage. This is one piece of a broader planned Quantum Meow MCP
ecosystem (a gateway/orchestrator server is planned separately —
this repo intentionally stays scoped to token market data only).
