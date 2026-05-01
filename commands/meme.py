from discord.ext import commands
import random

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        memes = ["💀 meme 1", "🔥 meme 2", "😂 meme 3"]
        await ctx.send(random.choice(memes))

async def setup(bot):
    await bot.add_cog(Meme(bot))