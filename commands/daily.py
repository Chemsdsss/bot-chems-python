from discord.ext import commands

balances = {}

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        user_id = ctx.author.id
        balances[user_id] = balances.get(user_id, 0) + 100

        await ctx.send("🎁 Tu as reçu 100 coins daily !")

async def setup(bot):
    await bot.add_cog(Daily(bot))