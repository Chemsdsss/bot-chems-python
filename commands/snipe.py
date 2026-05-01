from discord.ext import commands

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_message = None

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.last_message = message

    @commands.command()
    async def snipe(self, ctx):
        if self.last_message:
            await ctx.send(self.last_message.content)
        else:
            await ctx.send("Rien à snipe.")

async def setup(bot):
    await bot.add_cog(Snipe(bot))