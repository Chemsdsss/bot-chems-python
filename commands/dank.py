from discord.ext import commands
import random

class Dank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dank(self, ctx):
        memes = [
            "💀 Quand tu dis 'je viens vite' et ça fait 2h",
            "🧠 Moi après 2h de code : ça marche toujours pas",
            "📉 Motivation: 100% → 0% en 1 minute",
            "👀 Je fais semblant de comprendre alors que non",
            "🔥 Ce code marche... (mensonge)"
        ]

        await ctx.send(f"😂 {random.choice(memes)}")

async def setup(bot):
    await bot.add_cog(Dank(bot))