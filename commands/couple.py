from discord.ext import commands
import random

class Couple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def couple(self, ctx, user1: str = None, user2: str = None):
        if not user1 or not user2:
            return await ctx.send("❌ Utilisation : !couple @user1 @user2")

        percent = random.randint(0, 100)

        await ctx.send(
            f"💞 Couple : {user1} ❤️ {user2}\n"
            f"Compatibilité : **{percent}%**"
        )

async def setup(bot):
    await bot.add_cog(Couple(bot))