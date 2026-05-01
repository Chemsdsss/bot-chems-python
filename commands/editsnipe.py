from discord.ext import commands

class EditSnipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def editsnipe(self, ctx):
        data = getattr(self.bot, "last_edit", None)

        if not data or ctx.channel.id not in data:
            return await ctx.send("❌ Aucun edit à sniper.")

        edit = data[ctx.channel.id]

        await ctx.send(
            f"✏️ **Edit Snipe**\n"
            f"👤 {edit['author']}\n"
            f"➡️ Avant : {edit['before']}\n"
            f"➡️ Après : {edit['after']}"
        )

async def setup(bot):
    await bot.add_cog(EditSnipe(bot))