import discord
from discord.ext import commands
from utility.logger import Logger
from utility.env import Env
from utility.config import Config
import os
import asyncio

# Utility Setup
logger: Logger = Logger()
env: Env = Env()
config: Config = Config()

# Bot Setup
bot: commands.Bot = commands.Bot(command_prefix=config.command_prefix, intents=discord.Intents().all())

# Startup
@bot.event
async def on_ready() -> None:
    logger.log("Bot On.")

    # Add Status
    if config.check_discord_status:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(config.discord_status))
    else:
        await bot.change_presence(status=discord.Status.online)

# Loads all cogs in /bot/cogs
async def load_cogs() -> None:
    for cog in os.listdir("./bot/cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(env.discord_token)

asyncio.run(main())