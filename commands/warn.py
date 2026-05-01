from discord.ext import commands

warnings = {}

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason="Aucune raison"):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        user_id = member.id

        if user_id not in warnings:
            warnings[user_id] = []

        warnings[user_id].append(reason)

        await ctx.send(f"⚠️ {member.mention} a été warn.\nRaison : {reason}")

async def setup(bot):
    await bot.add_cog(Warn(bot))