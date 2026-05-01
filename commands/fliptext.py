from discord.ext import commands

class FlipText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fliptext(self, ctx, *, text):
        flipped = text[::-1]
        await ctx.send(f"🔁 {flipped}")

async def setup(bot):
    await bot.add_cog(FlipText(bot))