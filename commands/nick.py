from discord.ext import commands

class Nick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nick(self, ctx, member: commands.MemberConverter, *, name):
        await member.edit(nick=name)
        await ctx.send(f"✏️ Nick changé pour {member}")

async def setup(bot):
    await bot.add_cog(Nick(bot))