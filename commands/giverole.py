from discord.ext import commands

class Give(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def give(self, ctx, member, item):
        await ctx.send(f"🎁 {ctx.author} donne {item} à {member}")

async def setup(bot):
    await bot.add_cog(Give(bot))