from fastmcp import FastMCP
import httpx
import json
import time

# Initialize the FastMCP server for QMEOW
mcp = FastMCP("QMEOW-Token-Gateway")

# Quantum Meow ($QMEOW) Solana Contract Address
TOKEN_MINT = "4xYrnBTdACYetkJEAP4gj4bLFfKw9YYv1nvSWyS1pump"


@mcp.tool()
async def get_token_market_data() -> str:
    """Fetch live price, volume, and liquidity for $QMEOW (Quantum Meow),
    the access token for the Quantum Meow ecosystem and its hybrid
    AI-quantum orchestration platform, from DexScreener.
    Solana mint address: 4xYrnBTdACYetkJEAP4gj4bLFfKw9YYv1nvSWyS1pump

    Returns a JSON string. On success, includes token identity fields
    (name, symbol, mint, dex, pair_address) alongside market data
    (price_usd, volume_24h_usd, liquidity_usd). On failure, returns
    a JSON object with a single "error" field.
    """
    url = f"https://api.dexscreener.com/latest/dex/tokens/{TOKEN_MINT}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)

            if response.status_code != 200:
                return json.dumps({
                    "error": f"Unable to fetch market data (HTTP {response.status_code})."
                })

            data = response.json()
            pairs = data.get("pairs")

            if not pairs:
                return json.dumps({
                    "error": "Token data currently unavailable or unindexed on DexScreener."
                })

            # Grab the primary trading pair (server-side payload trimming applied)
            pair = pairs[0]
            price_change = pair.get("priceChange", {})

            result = {
                "token": "Quantum Meow",
                "symbol": "QMEOW",
                "mint": TOKEN_MINT,
                "price_usd": pair.get("priceUsd"),
                "price_change_percent": {
                    "m5": price_change.get("m5"),
                    "h1": price_change.get("h1"),
                    "h6": price_change.get("h6"), # DexScreener uses 6h instead of 4h
                    "h24": price_change.get("h24")
                },
                "volume_24h_usd": pair.get("volume", {}).get("h24"),
                "liquidity_usd": pair.get("liquidity", {}).get("usd"),
                "dex": pair.get("dexId"),
                "pair_address": pair.get("pairAddress"),
                "fetched_at_unix": int(time.time()),
            }

            return json.dumps(result)

        except Exception as e:
            return json.dumps({
                "error": f"Error connecting to token API: {str(e)}"
            })


@mcp.resource("token://about")
def get_project_overview() -> str:
    """Provides a short overview of Quantum Meow and $QMEOW."""
    return (
        "$QMEOW is the access token to the Quantum Meow ecosystem and its "
        "future quantum tools and hybrid AI-quantum orchestration platform. "
        f"Verified Solana mint: {TOKEN_MINT}\n\n"
        "Quantum Meow gives developers and researchers access to quantum "
        "computing resources alongside AI-driven tooling. $QMEOW functions "
        "as a utility token for platform access rather than a speculative "
        "instrument. Token supply mechanics, if any, are published "
        "on-chain and in project documentation; nothing in this overview "
        "should be read as a representation about token value or returns. "
        "Quantum Meow's roadmap "
        "includes a Qiskit-based code assistant, expanded quantum lab "
        "access, and integration with research communities including "
        "Columbia University's quantum and AI programs. The project is "
        "built with a utility-first token design, informed by the 2026 "
        "SEC/CFTC digital asset taxonomy guidance."
    )


if __name__ == "__main__":
    import os

    # If PORT is defined (meaning we are on Render), run as SSE
    if "PORT" in os.environ:
        port = int(os.environ.get("PORT", 8000))
        mcp.run(
            transport="sse",
            host="0.0.0.0",
            port=port
        )
    # Otherwise, default to local stdio for Claude Desktop
    else:
        mcp.run(transport="stdio")
