"""
PumpFun Trading Bot — Main Runner
"""

import asyncio
import os
import sys
import yaml
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("pump_bot")


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


async def run_bot(config: dict):
    platform = config.get("platform", "pump_fun")
    logger.info(f"Starting bot for platform: {platform}")
    logger.info(f"Max RPS: {config.get('max_rps', 25)}")
    logger.info(f"Subscription method: {config.get('subscription_method', 'logs')}")
    logger.info(f"Buy amount: {config.get('buy_amount_sol', 0.01)} SOL")
    logger.info(f"Take profit: {config.get('take_profit_pct', 50)}%")
    logger.info(f"Stop loss: {config.get('stop_loss_pct', 20)}%")

    rpc = os.getenv("RPC_ENDPOINT")
    if not rpc:
        logger.error("RPC_ENDPOINT not set in .env — please configure it first.")
        sys.exit(1)

    logger.info("Bot initialized. Listening for new tokens...")

    # Main loop placeholder
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")


def main():
    config_path = Path("bots/pumpfun_bot.yaml")
    if not config_path.exists():
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)

    config = load_config(str(config_path))
    asyncio.run(run_bot(config))


if __name__ == "__main__":
    main()
