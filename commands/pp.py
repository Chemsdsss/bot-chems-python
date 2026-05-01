from discord.ext import commands
import random

class PP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pp(self, ctx, member=None):
        member = member or ctx.author

        size = random.randint(1, 30)
        bar = "8" + "=" * size + "D"

        await ctx.send(f"🍆 PP de {member.mention} : {bar} ({size} cm)")

async def setup(bot):
    await bot.add_cog(PP(bot))