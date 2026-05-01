from discord.ext import commands
import random

class Ball8(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def ball(self, ctx, *, question):
        responses = ["Oui", "Non", "Peut-être", "Impossible", "Certainement"]
        await ctx.send(random.choice(responses))

async def setup(bot):
    await bot.add_cog(Ball8(bot))