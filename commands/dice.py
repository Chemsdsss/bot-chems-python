from discord.ext import commands
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        await ctx.send(f"🎲 {random.randint(1, 6)}")

async def setup(bot):
    await bot.add_cog(Dice(bot))