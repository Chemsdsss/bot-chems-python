from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def music(self, ctx, *, song):
        await ctx.send(f"🎵 Lecture : {song} (systeme à connecter)")

async def setup(bot):
    await bot.add_cog(Music(bot))