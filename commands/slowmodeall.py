from discord.ext import commands

class SlowmodeAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmodeall(self, ctx, seconds: int):
        for channel in ctx.guild.text_channels:
            await channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slowmode appliqué partout : {seconds}s")

async def setup(bot):
    await bot.add_cog(SlowmodeAll(bot))