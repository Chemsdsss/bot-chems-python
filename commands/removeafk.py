from discord.ext import commands

class RemoveAFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk = {}

    @commands.command()
    async def removeafk(self, ctx):
        if ctx.author.id in self.afk:
            del self.afk[ctx.author.id]
            await ctx.send(f"🟢 {ctx.author.mention} n’est plus AFK.")
        else:
            await ctx.send("❌ Tu n’es pas AFK.")

async def setup(bot):
    await bot.add_cog(RemoveAFK(bot))