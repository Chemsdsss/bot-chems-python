from discord.ext import commands

balances = {}

class Buy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ctx, item):
        await ctx.send(f"🛒 Tu as essayé d’acheter {item} (système à compléter).")

async def setup(bot):
    await bot.add_cog(Buy(bot))