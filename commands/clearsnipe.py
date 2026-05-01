from discord.ext import commands

class ClearSnipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipe = {}  # Un dictionnaire pour stocker les derniers messages supprimés

    @commands.command()
    async def clearsnipe(self, ctx):
        if ctx.author.id != ctx.bot.owner_id:
            return await ctx.send("❌ Vous devez être l'owner pour cette commande.")

        self.snipe.clear()  # Efface tous les messages "snipe"
        await ctx.send("🧹 Les messages de snipe ont été effacés.")

async def setup(bot):
    await bot.add_cog(ClearSnipe(bot))