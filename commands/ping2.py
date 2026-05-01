from discord.ext import commands
import time

class Ping2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping2(self, ctx):
        start = time.time()
        msg = await ctx.send("📡 Ping...")
        end = time.time()

        await msg.edit(
            content=f"🏓 Pong !\n"
                    f"Bot latency: {round(self.bot.latency * 1000)}ms\n"
                    f"Message latency: {round((end - start) * 1000)}ms"
        )

async def setup(bot):
    await bot.add_cog(Ping2(bot))