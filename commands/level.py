from discord.ext import commands

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.levels = {}

    @commands.command()
    async def level(self, ctx):
        lvl = self.levels.get(ctx.author.id, 1)
        await ctx.send(f"⭐ Niveau : {lvl}")

async def setup(bot):
    await bot.add_cog(Level(bot))