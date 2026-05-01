from discord.ext import commands

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx):
        await ctx.send(
            "🛒 Boutique :\n"
            "1. Sword - 500 coins\n"
            "2. Shield - 300 coins\n"
            "3. VIP - 1000 coins"
        )

async def setup(bot):
    await bot.add_cog(Shop(bot))