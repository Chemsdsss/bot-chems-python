from discord.ext import commands

class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slowmode : {seconds}s")

async def setup(bot):
    await bot.add_cog(Slowmode(bot))