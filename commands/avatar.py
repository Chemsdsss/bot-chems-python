from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member=None):
        member = member or ctx.author
        await ctx.send(member.avatar.url)

async def setup(bot):
    await bot.add_cog(Avatar(bot))