from discord.ext import commands

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        await ctx.send(
            f"🤖 Bot : {self.bot.user}\n"
            f"Serveurs : {len(self.bot.guilds)}"
        )

async def setup(bot):
    await bot.add_cog(BotInfo(bot))