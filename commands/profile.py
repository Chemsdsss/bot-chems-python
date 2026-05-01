from discord.ext import commands

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member=None):
        member = member or ctx.author

        await ctx.send(
            f"👤 Profil de {member}\n"
            f"ID : {member.id}\n"
            f"Compte créé : {member.created_at}"
        )

async def setup(bot):
    await bot.add_cog(Profile(bot))