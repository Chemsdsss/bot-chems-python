from discord.ext import commands
import asyncio

class FakeHack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fakehack(self, ctx, member=None):
        member = member or ctx.author

        msg = await ctx.send(f"💻 Hack de {member} en cours...")

        steps = [
            "Connexion aux serveurs Discord...",
            "Récupération des données...",
            "Bypass sécurité...",
            "Extraction messages privés...",
            "Injection virus 🦠...",
            "Finition du hack..."
        ]

        for step in steps:
            await asyncio.sleep(1)
            await msg.edit(content=f"💻 Hack de {member}\n\n{step}")

        await asyncio.sleep(1)
        await msg.edit(
            content=f"💀 {member} a été hack (FAKE 😈)\n"
                    f"📁 Données : [rires détectés]"
        )

async def setup(bot):
    await bot.add_cog(FakeHack(bot))