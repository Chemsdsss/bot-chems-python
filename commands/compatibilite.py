from discord.ext import commands
import random

class Compatibles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def compatibles(self, ctx, member1=None, member2=None):
        member1 = member1 or ctx.author.mention

        if not member2:
            member2 = random.choice(ctx.guild.members).mention

        percent = random.randint(0, 100)

        if percent > 80:
            emoji = "💖"
        elif percent > 50:
            emoji = "💘"
        else:
            emoji = "💔"

        await ctx.send(
            f"💞 Compatibilité : {member1} + {member2}\n"
            f"{emoji} Score : **{percent}%**"
        )

async def setup(bot):
    await bot.add_cog(Compatibles(bot))