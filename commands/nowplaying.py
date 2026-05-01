from discord.ext import commands

class NowPlaying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nowplaying(self, ctx):
        await ctx.send("🎵 Rien en cours de lecture.")

async def setup(bot):
    await bot.add_cog(NowPlaying(bot))