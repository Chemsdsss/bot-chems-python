import discord
from discord.ext import commands
import os
import json
import asyncio

# =====================
# CONFIG LOAD
# =====================
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = config["token"]
PREFIX = config["prefix"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# =====================
# LOAD EXTENSIONS
# =====================
async def load_extensions():
    for file in os.listdir("./commands"):
        if file.endswith(".py"):
            ext = f"commands.{file[:-3]}"
            try:
                await bot.load_extension(ext)
                print(f"✅ Loaded {ext}")
            except Exception as e:
                print(f"❌ Error loading {ext}: {e}")

# =====================
# SETUP HOOK
# =====================
@bot.event
async def setup_hook():
    await load_extensions()

# =====================
# READY
# =====================
@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")
    print(f"📊 Servers: {len(bot.guilds)}")

    presence = config.get("presence", {})

    activity = discord.Game(name=presence.get("text", "Bot actif"))

    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )

# =====================
# ERROR HANDLER
# =====================
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Permissions manquantes.")
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await ctx.send(f"⚠️ Erreur: {error}")

# =====================
# RUN
# =====================
bot.run(TOKEN)