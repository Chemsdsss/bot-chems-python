from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: commands.MemberConverter, *, reason="Aucune raison"):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        await member.ban(reason=reason)
        await ctx.send(f"🔨 {member} a été banni.\nRaison : {reason}")

async def setup(bot):
    await bot.add_cog(Ban(bot))