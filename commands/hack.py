from discord.ext import commands
import asyncio

class Hack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hack(self, ctx, member=None):
        member = member or ctx.author

        msg = await ctx.send(f"💻 Hack de {member.mention} en cours...")

        steps = [
            "Connexion aux serveurs...",
            "Bypass firewall...",
            "Extraction données...",
            "Accès messages privés...",
            "Téléchargement fichiers...",
            "Finalisation..."
        ]

        for step in steps:
            await asyncio.sleep(1)
            await msg.edit(content=f"💻 Hack de {member.mention}\n\n{step}")

        await asyncio.sleep(1)

        await msg.edit(
            content=f"💀 {member.mention} a été 'hack' (FAKE 😈)\n"
                    f"📁 Données trouvées : [RIEN, c’est une blague]"
        )

async def setup(bot):
    await bot.add_cog(Hack(bot))