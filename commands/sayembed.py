from discord.ext import commands
import discord

class SayEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sayembed(self, ctx, *, message):
        embed = discord.Embed(description=message)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SayEmbed(bot))