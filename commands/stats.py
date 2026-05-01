from discord.ext import commands

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        await ctx.send(
            f"📊 Stats bot :\n"
            f"Serveurs : {len(self.bot.guilds)}\n"
            f"Utilisateurs : {sum(g.member_count for g in self.bot.guilds)}"
        )

async def setup(bot):
    await bot.add_cog(Stats(bot))