from discord.ext import commands

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def role(self, ctx, member: commands.MemberConverter, role: commands.RoleConverter):
        await member.add_roles(role)
        await ctx.send(f"🎭 {member.mention} a reçu {role.name}")

async def setup(bot):
    await bot.add_cog(Role(bot))