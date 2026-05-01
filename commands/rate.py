from discord.ext import commands
import random

class Rate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rate(self, ctx, *, thing=None):
        thing = thing or ctx.author.name

        score = random.randint(0, 100)

        if score <= 20:
            emoji = "💀"
        elif score <= 50:
            emoji = "😐"
        elif score <= 80:
            emoji = "🔥"
        else:
            emoji = "💯"

        await ctx.send(f"⭐ Je rate **{thing}** : {score}/100 {emoji}")

async def setup(bot):
    await bot.add_cog(Rate(bot))