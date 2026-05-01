from discord.ext import commands
import discord

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx, title, *, description):
        em = discord.Embed(title=title, description=description, color=0x00ffcc)
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(Embed(bot))