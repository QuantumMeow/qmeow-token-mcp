# QMEOW Token MCP

A local MCP server that exposes live price, volume, and liquidity data 
for $QMEOW (Solana) via DexScreener, for use with Claude Desktop and 
other MCP-compatible clients.

## Setup

```bash
pip install -r requirements.txt
python qmeow_token_mcp_server.py
```

## What it does

- `get_token_market_data()` — returns current price/volume/liquidity as JSON
- `token://about` — project overview resource

## Status

Early stage. Part of the broader Quantum Meow MCP ecosystem (gateway 
architecture planned — see [issues](link) for roadmap).
