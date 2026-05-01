import discord
from discord.ext import commands

@bot.command()
async def vote(ctx, *, question):
    embed = discord.Embed(
        title="🗳️ VOTE",
        description=question,
        color=discord.Color.blue()
    )

    msg = await ctx.send(embed=embed)

    await msg.add_reaction("👍")
    await msg.add_reaction("👎")