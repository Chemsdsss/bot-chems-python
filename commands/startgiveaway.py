import discord
from discord.ext import commands
import asyncio
import random
import re

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="+", intents=intents)

giveaways = {}

def parse_time(time_str):
    match = re.match(r"(\d+)(s|m|h|d)", time_str)
    if not match:
        return None

    value = int(match.group(1))
    unit = match.group(2)

    if unit == "s":
        return value
    if unit == "m":
        return value * 60
    if unit == "h":
        return value * 3600
    if unit == "d":
        return value * 86400

@bot.command()
async def giveaway(ctx, time: str, winners: int, *, prize: str):
    seconds = parse_time(time)

    if seconds is None:
        return await ctx.send("❌ Format invalide (ex: 10s, 5m, 2h, 1d)")

    embed = discord.Embed(
        title="🎉 GIVEAWAY 🎉",
        description=f"**Prix :** {prize}\n**Gagnants :** {winners}\n**Organisateur :** {ctx.author.mention}",
        color=discord.Color.red()
    )
    embed.set_footer(text="Réagis avec 🎉 pour participer !")

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎉")

    giveaways[msg.id] = {
        "prize": prize,
        "winners": winners,
        "channel": ctx.channel.id
    }

    await asyncio.sleep(seconds)

    new_msg = await ctx.channel.fetch_message(msg.id)
    reaction = discord.utils.get(new_msg.reactions, emoji="🎉")

    if reaction is None:
        return await ctx.send("❌ Aucun participant.")

    users = await reaction.users().flatten()
    users = [u for u in users if not u.bot]

    if len(users) == 0:
        return await ctx.send("❌ Aucun participant.")

    winners_list = random.sample(users, min(winners, len(users)))
    winners_mention = ", ".join([w.mention for w in winners_list])

    await ctx.send(f"🏆 **Gagnant(s)** : {winners_mention}\n🎁 **Prix** : {prize}")

bot.run("TON_TOKEN")