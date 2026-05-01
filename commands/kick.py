from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: commands.MemberConverter, *, reason="Aucune raison"):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        await member.kick(reason=reason)
        await ctx.send(f"👢 {member} a été kick.\nRaison : {reason}")

async def setup(bot):
    await bot.add_cog(Kick(bot))