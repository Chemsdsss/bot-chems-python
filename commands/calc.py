from discord.ext import commands

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, *, expression):
        try:
            result = eval(expression)
            await ctx.send(f"🧮 {result}")
        except:
            await ctx.send("❌ Expression invalide.")

async def setup(bot):
    await bot.add_cog(Calc(bot))