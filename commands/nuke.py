from discord.ext import commands

class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nuke(self, ctx):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        channel = ctx.channel
        new = await channel.clone()
        await channel.delete()

        await new.send("💥 Salon nuké.")

async def setup(bot):
    await bot.add_cog(Nuke(bot))