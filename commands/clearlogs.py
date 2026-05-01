from discord.ext import commands

class ClearLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clearlog(self, ctx):
        if not ctx.bot.is_owner_custom(ctx.author.id):
            return await ctx.send("❌ Vous devez être l'owner du bot pour cette commande.")

        # Supposons que tu as une liste de logs sauvegardée quelque part.
        # Tu peux remplacer ceci par un vrai système de gestion de logs
        await ctx.send("🧹 Effacement des logs...")
        # Ici, le code pour supprimer les logs réels (ex : fichier, base de données, etc.)
        # Par exemple : open("logs.txt", "w").close()

        await ctx.send("✅ Logs supprimés.")

async def setup(bot):
    await bot.add_cog(ClearLog(bot))