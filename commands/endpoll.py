from discord.ext import commands

class EndPoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def endpoll(self, ctx, message_id: int):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        try:
            msg = await ctx.channel.fetch_message(message_id)

            await msg.edit(content="🗳️ SONDAGE TERMINÉ")
            await ctx.send("✅ Poll terminé.")

        except:
            await ctx.send("❌ Message introuvable.")

async def setup(bot):
    await bot.add_cog(EndPoll(bot))