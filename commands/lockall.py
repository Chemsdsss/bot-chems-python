from discord.ext import commands

class LockAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lockall(self, ctx):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        for channel in ctx.guild.text_channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

        await ctx.send("🔒 Tous les salons sont lock.")

async def setup(bot):
    await bot.add_cog(LockAll(bot))