from discord.ext import commands
import discord

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason="Aucune raison"):
        # Vérif staff
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        # Cherche ou crée le rôle Muted
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role is None:
            role = await ctx.guild.create_role(name="Muted")

            # Désactiver permissions dans tous les salons
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False, speak=False)

        await member.add_roles(role, reason=reason)

        await ctx.send(f"🔇 {member.mention} a été mute.\nRaison : {reason}")

async def setup(bot):
    await bot.add_cog(Mute(bot))