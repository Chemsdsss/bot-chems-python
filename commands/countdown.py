from discord.ext import commands
import asyncio

class Countdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def countdown(self, ctx, seconds: int):
        for i in range(seconds, 0, -1):
            await ctx.send(i)
            await asyncio.sleep(1)

        await ctx.send("⏰ Terminé !")

async def setup(bot):
    await bot.add_cog(Countdown(bot))