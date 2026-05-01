from discord.ext import commands

class Banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banner(self, ctx, member=None):
        member = member or ctx.author

        user = await self.bot.fetch_user(member.id)
        if user.banner:
            await ctx.send(user.banner.url)
        else:
            await ctx.send("❌ Pas de banner.")

async def setup(bot):
    await bot.add_cog(Banner(bot))