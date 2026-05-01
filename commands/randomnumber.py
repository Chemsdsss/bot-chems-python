from discord.ext import commands
import random

class RandomNumber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomnumber(self, ctx, a: int = 1, b: int = 100):
        await ctx.send(f"🔢 Nombre : {random.randint(a, b)}")

async def setup(bot):
    await bot.add_cog(RandomNumber(bot))