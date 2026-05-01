from discord.ext import commands

class AntiBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            try:
                await member.ban(reason="Anti-bot system")
            except:
                pass

async def setup(bot):
    await bot.add_cog(AntiBot(bot))