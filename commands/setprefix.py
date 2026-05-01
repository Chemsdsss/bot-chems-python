from discord.ext import commands

class SetPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setprefix(self, ctx, prefix):
        await ctx.send(f"Prefix changé en : {prefix}")

async def setup(bot):
    await bot.add_cog(SetPrefix(bot))