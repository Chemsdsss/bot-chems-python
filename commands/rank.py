from discord.ext import commands

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rank(self, ctx):
        await ctx.send(f"🏆 Rank de {ctx.author.name} : Bronze (exemple)")

async def setup(bot):
    await bot.add_cog(Rank(bot))