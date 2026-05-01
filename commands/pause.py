from discord.ext import commands

class Pause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pause(self, ctx):
        await ctx.send("⏸️ Musique en pause")

async def setup(bot):
    await bot.add_cog(Pause(bot))