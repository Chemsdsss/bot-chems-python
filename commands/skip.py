from discord.ext import commands

class Skip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skip(self, ctx):
        await ctx.send("Musique skip.")

async def setup(bot):
    await bot.add_cog(Skip(bot))