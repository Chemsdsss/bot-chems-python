from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, question):
        msg = await ctx.send(f"📊 {question}\n👍 Oui | 👎 Non")
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

async def setup(bot):
    await bot.add_cog(Poll(bot))