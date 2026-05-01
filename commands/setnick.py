from discord.ext import commands

class SetNick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setnick(self, ctx, member: commands.MemberConverter, *, nick):
        await member.edit(nick=nick)
        await ctx.send("Pseudo modifié.")

async def setup(bot):
    await bot.add_cog(SetNick(bot))