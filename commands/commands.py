from discord.ext import commands

class CommandList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commandlist(self, ctx):
        commands = [command.name for command in self.bot.commands]
        await ctx.send(f"📜 Liste des commandes : \n{', '.join(commands)}")

async def setup(bot):
    await bot.add_cog(CommandList(bot))