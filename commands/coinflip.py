from discord.ext import commands
import random

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        result = random.choice(["Pile 🪙", "Face 🪙"])
        await ctx.send(f"Résultat : {result}")

async def setup(bot):
    await bot.add_cog(Coinflip(bot))