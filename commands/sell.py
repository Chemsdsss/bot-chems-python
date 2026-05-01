from discord.ext import commands

class Sell(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sell(self, ctx, item=None):
        if not item:
            await ctx.send("Tu dois préciser un objet.")
        else:
            await ctx.send(f"Objet vendu : {item}")

async def setup(bot):
    await bot.add_cog(Sell(bot))