from discord.ext import commands

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, song):
        await ctx.send(f"🎵 Lecture : {song} (system à connecter)")

async def setup(bot):
    await bot.add_cog(Play(bot))