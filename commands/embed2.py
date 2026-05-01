from discord.ext import commands
import discord

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx, title, *, description):
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.blurple()
        )

        embed.set_footer(text=f"Demandé par {ctx.author.name}")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Embed(bot))