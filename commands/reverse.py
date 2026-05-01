from discord.ext import commands

class Reverse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reverse(self, ctx, *, text):
        await ctx.send(text[::-1])

async def setup(bot):
    await bot.add_cog(Reverse(bot))