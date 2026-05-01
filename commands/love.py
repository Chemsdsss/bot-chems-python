from discord.ext import commands
import random

class Love(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def love(self, ctx, member):
        percent = random.randint(0, 100)
        await ctx.send(f"❤️ Compatibilité {ctx.author.mention} + {member} : {percent}%")

async def setup(bot):
    await bot.add_cog(Love(bot))