from discord.ext import commands

class DM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dm(self, ctx, member: commands.MemberConverter, *, message):
        try:
            await member.send(message)
            await ctx.send("📩 Message envoyé en DM.")
        except:
            await ctx.send("❌ Impossible d’envoyer le DM.")

async def setup(bot):
    await bot.add_cog(DM(bot))