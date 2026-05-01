from discord.ext import commands

class Queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}

    @commands.command()
    async def queue(self, ctx):
        guild_id = ctx.guild.id

        queue = self.queues.get(guild_id, [])

        if not queue:
            return await ctx.send("📭 Queue vide.")

        msg = "🎵 **Queue :**\n"
        for i, song in enumerate(queue[:10], 1):
            msg += f"{i}. {song}\n"

        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(Queue(bot))