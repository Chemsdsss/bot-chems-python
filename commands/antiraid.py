from discord.ext import commands

class AntiRaid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def antiraid(self, ctx):
        if not ctx.bot.is_owner_custom(ctx.author.id):
            return await ctx.send("❌ Owner uniquement.")

        await ctx.send("🛡️ Anti-raid activé (mode simple).")

async def setup(bot):
    await bot.add_cog(AntiRaid(bot))