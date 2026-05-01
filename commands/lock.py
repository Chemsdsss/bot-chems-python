from discord.ext import commands

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lock(self, ctx):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False

        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        await ctx.send("🔒 Salon verrouillé.")

async def setup(bot):
    await bot.add_cog(Lock(bot))