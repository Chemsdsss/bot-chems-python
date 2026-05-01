from discord.ext import commands

class Kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, member):
        await ctx.send(f"{ctx.author.mention} embrasse {member} 😘")

async def setup(bot):
    await bot.add_cog(Kiss(bot))