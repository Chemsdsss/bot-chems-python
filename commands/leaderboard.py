from discord.ext import commands

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leaderboard(self, ctx):
        eco = self.bot.economy
        top = sorted(eco.items(), key=lambda x: x[1], reverse=True)[:5]

        msg = "🏆 Leaderboard :\n"
        for i, (user, bal) in enumerate(top, 1):
            msg += f"{i}. <@{user}> - {bal} coins\n"

        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(Leaderboard(bot))