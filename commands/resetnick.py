from discord.ext import commands

class ResetNick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def resetnick(self, ctx, member: commands.MemberConverter):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        await member.edit(nick=None)
        await ctx.send(f"🔄 Nickname reset pour {member.mention}")

async def setup(bot):
    await bot.add_cog(ResetNick(bot))