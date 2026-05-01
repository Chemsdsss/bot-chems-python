from discord.ext import commands
import random

class Punch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, ctx, member=None):
        member = member or ctx.author

        damage = random.randint(1, 100)

        reactions = [
            "💥 BAM !",
            "👊 BOUM !",
            "💢 CRACK !",
            "😵 KO !"
        ]

        await ctx.send(
            f"{random.choice(reactions)} {ctx.author.mention} frappe {member.mention}\n"
            f"💥 Dégâts : {damage}%"
        )

async def setup(bot):
    await bot.add_cog(Punch(bot))