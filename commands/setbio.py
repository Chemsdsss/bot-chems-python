from discord.ext import commands

class SetBio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setbio(self, ctx, *, bio):
        await ctx.send("Bio mise à jour (fake).")

async def setup(bot):
    await bot.add_cog(SetBio(bot))