from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def logs(self, ctx):
        await ctx.send("📜 Système de logs actif (à configurer)")

async def setup(bot):
    await bot.add_cog(Logs(bot))