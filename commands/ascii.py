from discord.ext import commands

class Ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ascii(self, ctx, *, text):
        await ctx.send(f"```\n{text}\n```")

async def setup(bot):
    await bot.add_cog(Ascii(bot))