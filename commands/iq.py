from discord.ext import commands
import random

class IQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def iq(self, ctx, member=None):
        iq = random.randint(30, 180)
        await ctx.send(f"🧠 IQ de {member or ctx.author.name} : {iq}")

async def setup(bot):
    await bot.add_cog(IQ(bot))