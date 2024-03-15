import discord
from discord.ext import commands
from utility.logger import Logger
from utility.env import Env
import os
import asyncio

# CLI Variables
journal_type: str = "print"

# Config
command_prefix: str = "$"
discord_game: str = "Game"
discord_status: bool = True

# Utility Setup
logger: Logger = Logger(journal_type=journal_type)
env: Env = Env()

# Bot Setup
bot: commands.Bot = commands.Bot(command_prefix=command_prefix, intents=discord.Intents().all())

# Startup
@bot.event
async def on_ready() -> None:
    logger.log("Bot On.")

    # Add Status
    if discord_status:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(discord_game))

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