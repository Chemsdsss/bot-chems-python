from discord.ext import commands

class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unlock(self, ctx):
        if not ctx.bot.is_staff_custom(ctx.author):
            return await ctx.send("❌ Permission refusée.")

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True

        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        await ctx.send("🔓 Salon déverrouillé.")

async def setup(bot):
    await bot.add_cog(Unlock(bot))