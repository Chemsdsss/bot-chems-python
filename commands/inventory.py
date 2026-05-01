from discord.ext import commands

inventory = {}

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inventory(self, ctx):
        items = inventory.get(ctx.author.id, [])

        if not items:
            return await ctx.send("🎒 Inventaire vide.")

        await ctx.send("🎒 Inventaire : " + ", ".join(items))

async def setup(bot):
    await bot.add_cog(Inventory(bot))