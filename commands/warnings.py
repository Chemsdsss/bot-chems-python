from discord.ext import commands

warnings = {}

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warnings(self, ctx, member: discord.Member):
        if member.id not in warnings or len(warnings[member.id]) == 0:
            return await ctx.send("✅ Aucun warn.")

        liste = "\n".join(warnings[member.id])

        await ctx.send(f"⚠️ Warns de {member} :\n{liste}")

async def setup(bot):
    await bot.add_cog(Warnings(bot))