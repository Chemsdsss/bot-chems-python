from discord.ext import commands
import random

class Ship(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ship(self, ctx, user1: commands.MemberConverter, user2: commands.MemberConverter):
        percent = random.randint(0, 100)
        if percent < 30:
            msg = "💔 Mauvais match..."
        elif percent < 70:
            msg = "💛 Ça passe..."
        else:
            msg = "❤️ Couple parfait !"

        await ctx.send(f"{user1.mention} ❤️ {user2.mention} = **{percent}%**\n{msg}")

async def setup(bot):
    await bot.add_cog(Ship(bot))