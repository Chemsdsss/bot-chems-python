from discord.ext import commands

class Shutdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shutdown(self, ctx):
        if not ctx.bot.is_owner_custom(ctx.author.id):
            return await ctx.send("❌ Owner uniquement.")

        await ctx.send("🛑 Arrêt du bot...")
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(Shutdown(bot))