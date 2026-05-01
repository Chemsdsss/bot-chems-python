from discord.ext import commands

class ModLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def modlogs(self, ctx):
        await ctx.send("📜 Logs modération actifs (à configurer)")

async def setup(bot):
    await bot.add_cog(ModLogs(bot))