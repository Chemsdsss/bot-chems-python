from discord.ext import commands

class Resume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def resume(self, ctx):
        await ctx.send("▶️ Musique reprise")

async def setup(bot):
    await bot.add_cog(Resume(bot))