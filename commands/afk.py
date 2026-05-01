from discord.ext import commands

afk_users = {}

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx, *, reason="AFK"):
        afk_users[ctx.author.id] = reason
        await ctx.send(f"😴 {ctx.author.mention} est AFK : {reason}")

async def setup(bot):
    await bot.add_cog(AFK(bot))