from discord.ext import commands

class Slap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, member):
        await ctx.send(f"{ctx.author.mention} gifle {member} 👋💥")

async def setup(bot):
    await bot.add_cog(Slap(bot))