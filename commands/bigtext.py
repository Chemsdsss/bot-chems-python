from discord.ext import commands

class BigText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bigtext(self, ctx, *, text):
        await ctx.send("🅱️ " + " ".join(text.upper()))

async def setup(bot):
    await bot.add_cog(BigText(bot))