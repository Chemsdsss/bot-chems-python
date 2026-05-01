from discord.ext import commands

class Loop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.looping = {}

    @commands.command()
    async def loop(self, ctx):
        guild_id = ctx.guild.id

        self.looping[guild_id] = not self.looping.get(guild_id, False)

        state = "activé 🔁" if self.looping[guild_id] else "désactivé ❌"

        await ctx.send(f"🔁 Loop {state}")

async def setup(bot):
    await bot.add_cog(Loop(bot))