from discord.ext import commands

class DMAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dmall(self, ctx, *, message):
        if not ctx.bot.is_owner_custom(ctx.author.id):
            return await ctx.send("❌ Owner uniquement.")

        for member in ctx.guild.members:
            try:
                await member.send(message)
            except:
                pass

        await ctx.send("📩 DM envoyés à tous.")

async def setup(bot):
    await bot.add_cog(DMAll(bot))