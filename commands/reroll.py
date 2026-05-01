from discord.ext import commands

class Repeat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.repeat = {}

    @commands.command()
    async def repeat(self, ctx):
        guild_id = ctx.guild.id
        self.repeat[guild_id] = not self.repeat.get(guild_id, False)

        state = "ON 🔁" if self.repeat[guild_id] else "OFF ❌"
        await ctx.send(f"🔁 Repeat : {state}")

async def setup(bot):
    await bot.add_cog(Repeat(bot))