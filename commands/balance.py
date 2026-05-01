from discord.ext import commands

balances = {}

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx, member=None):
        member = member or ctx.author
        user_id = member.id

        bal = balances.get(user_id, 0)
        await ctx.send(f"💰 {member.mention} a {bal} coins.")

async def setup(bot):
    await bot.add_cog(Balance(bot))