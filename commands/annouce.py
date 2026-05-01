from discord.ext import commands

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def announce(self, ctx, *, message):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        await ctx.send(f"📢 **Annonce :**\n{message}")

async def setup(bot):
    await bot.add_cog(Announce(bot))