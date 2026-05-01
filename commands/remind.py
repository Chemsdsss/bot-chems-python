from discord.ext import commands
import asyncio

class Remind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remind(self, ctx, time: int, *, text):
        await ctx.send(f"⏰ Je te rappelle dans {time} secondes.")

        await asyncio.sleep(time)

        await ctx.send(f"🔔 {ctx.author.mention} rappel : {text}")

async def setup(bot):
    await bot.add_cog(Remind(bot))