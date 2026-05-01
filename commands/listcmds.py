from discord.ext import commands

class ListCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def listcmds(self, ctx):
        cmds = [c.name for c in self.bot.commands]
        await ctx.send("📜 " + ", ".join(cmds))

async def setup(bot):
    await bot.add_cog(ListCmds(bot))