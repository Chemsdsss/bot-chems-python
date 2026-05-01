from discord.ext import commands
import discord

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"🔊 {member.mention} a été unmute.")
        else:
            await ctx.send("⚠️ Cette personne n'est pas mute.")

async def setup(bot):
    await bot.add_cog(Unmute(bot))