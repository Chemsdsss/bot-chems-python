from discord.ext import commands

class Softban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await ctx.guild.ban(member, reason=reason)
        await ctx.guild.unban(member)
        await ctx.send(f"{member} a été softban.")

async def setup(bot):
    await bot.add_cog(Softban(bot))