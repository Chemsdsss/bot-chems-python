from discord.ext import commands

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.prefix = "!"

    @commands.command()
    async def setprefix(self, ctx, new_prefix):
        self.prefix = new_prefix
        await ctx.send(f"🔧 Prefix changé en `{new_prefix}`")

async def setup(bot):
    await bot.add_cog(Prefix(bot))