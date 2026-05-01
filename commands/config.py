from discord.ext import commands

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def config(self, ctx):
        if not ctx.bot.is_owner_custom(ctx.author.id):
            return await ctx.send("❌ Owner uniquement.")

        await ctx.send("⚙️ Config du bot chargée.")

async def setup(bot):
    await bot.add_cog(Config(bot))