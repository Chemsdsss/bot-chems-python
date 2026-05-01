from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gamble(self, ctx, amount: int):
        eco = self.bot.economy

        if amount <= 0:
            return await ctx.send("❌ Montant invalide.")

        balance = eco.get(ctx.author.id, 0)

        if balance < amount:
            return await ctx.send("❌ Pas assez d'argent.")

        result = random.choice(["win", "lose", "lose"])

        if result == "win":
            eco[ctx.author.id] += amount
            await ctx.send(f"🎰 Tu as gagné ! +{amount} coins")
        else:
            eco[ctx.author.id] -= amount
            await ctx.send(f"💀 Tu as perdu ! -{amount} coins")

async def setup(bot):
    await bot.add_cog(Gamble(bot))