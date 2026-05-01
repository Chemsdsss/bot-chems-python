from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unban(self, ctx, user_id: int):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        user = await self.bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"✅ {user} a été débanni.")

async def setup(bot):
    await bot.add_cog(Unban(bot))