from discord.ext import commands

class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("Musique arrêtée.")

async def setup(bot):
    await bot.add_cog(Stop(bot))