from discord.ext import commands

class Hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member):
        await ctx.send(f"{ctx.author.mention} fait un câlin à {member} 🤗")

async def setup(bot):
    await bot.add_cog(Hug(bot))