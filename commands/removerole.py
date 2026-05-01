from discord.ext import commands

class Remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remove(self, ctx, member: commands.MemberConverter, role: commands.RoleConverter):
        await member.remove_roles(role)
        await ctx.send(f"❌ {role.name} retiré à {member}")

async def setup(bot):
    await bot.add_cog(Remove(bot))