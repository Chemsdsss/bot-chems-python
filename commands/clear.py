from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        await ctx.channel.purge(limit=amount)
        await ctx.send(f"🧹 {amount} messages supprimés.", delete_after=3)

async def setup(bot):
    await bot.add_cog(Clear(bot))