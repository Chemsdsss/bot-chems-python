from discord.ext import commands

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        jokes = [
            "Pourquoi les plongeurs plongent toujours en arrière ?",
            "Parce que sinon ils tombent dans le bateau 😭"
        ]
        await ctx.send(jokes[0])

async def setup(bot):
    await bot.add_cog(Joke(bot))