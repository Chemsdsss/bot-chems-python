from discord.ext import commands

class SetAvatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setavatar(self, ctx, url):
        await ctx.send("Fonction non implémentée.")

async def setup(bot):
    await bot.add_cog(SetAvatar(bot))