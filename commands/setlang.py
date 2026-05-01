from discord.ext import commands

class SetLang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setlang(self, ctx, lang):
        await ctx.send(f"Langue définie sur : {lang}")

async def setup(bot):
    await bot.add_cog(SetLang(bot))