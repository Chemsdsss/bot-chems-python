from discord.ext import commands
import random

class Gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gay(self, ctx, member=None):
        member = member or ctx.author
        percent = random.randint(0, 100)
        await ctx.send(f"🏳️‍🌈 {member} est {percent}% gay")

async def setup(bot):
    await bot.add_cog(Gay(bot))