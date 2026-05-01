from discord.ext import commands

class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveaway(self, ctx, *, prize):
        await ctx.send(f"🎁 GIVEAWAY : {prize}\nRéagis 🎉 pour participer !")

async def setup(bot):
    await bot.add_cog(Giveaway(bot))