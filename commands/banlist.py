from discord.ext import commands

class BanList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banlist(self, ctx):
        bans = await ctx.guild.bans()
        await ctx.send(f"📜 Bans : {len(bans)}")

async def setup(bot):
    await bot.add_cog(BanList(bot))