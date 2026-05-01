from discord.ext import commands

balances = {}

class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pay(self, ctx, member: commands.MemberConverter, amount: int):
        if amount <= 0:
            return await ctx.send("❌ Montant invalide.")

        balances[ctx.author.id] = balances.get(ctx.author.id, 0)
        balances[member.id] = balances.get(member.id, 0)

        if balances[ctx.author.id] < amount:
            return await ctx.send("❌ Pas assez d'argent.")

        balances[ctx.author.id] -= amount
        balances[member.id] += amount

        await ctx.send(f"💸 {ctx.author.mention} a payé {member.mention} {amount} coins.")

async def setup(bot):
    await bot.add_cog(Pay(bot))