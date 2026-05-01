from discord.ext import commands
import discord

class AddRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        await member.add_roles(role)
        await ctx.send(f"➕ Role {role.name} ajouté à {member}")

async def setup(bot):
    await bot.add_cog(AddRole(bot))