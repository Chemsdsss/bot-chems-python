from discord.ext import commands
import time
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns = {}

    def get_bal(self, user_id):
        eco = self.bot.economy
        return eco.get(user_id, 0)

    def add_money(self, user_id, amount):
        eco = self.bot.economy
        eco[user_id] = eco.get(user_id, 0) + amount

    def remove_money(self, user_id, amount):
        eco = self.bot.economy
        eco[user_id] = eco.get(user_id, 0) - amount

    @commands.command()
    async def economy(self, ctx, action=None, member=None, amount: int = None):
        user = ctx.author

        # 💰 BALANCE
        if action == "balance":
            target = member or user
            bal = self.get_bal(target.id)
            return await ctx.send(f"💰 {target.mention} : **{