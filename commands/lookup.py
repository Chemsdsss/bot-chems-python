from discord.ext import commands

class Lookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookup(self, ctx, user: commands.MemberConverter):
        await ctx.send(f"🔍 Infos sur {user} : ID {user.id}")

async def setup(bot):
    await bot.add_cog(Lookup(bot))