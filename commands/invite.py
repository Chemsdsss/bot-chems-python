from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("🔗 Invite ton bot via Discord Developer Portal (ou lien à configurer).")

async def setup(bot):
    await bot.add_cog(Invite(bot))