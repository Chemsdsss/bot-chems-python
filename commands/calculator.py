from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calculator(self, ctx, *, expression: str):
        try:
            # on évalue l'expression donnée par l'utilisateur
            result = eval(expression)
            await ctx.send(f"🧮 Résultat : {result}")
        except Exception as e:
            await ctx.send(f"❌ Erreur : {e}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))