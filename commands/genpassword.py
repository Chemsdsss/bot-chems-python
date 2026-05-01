from discord.ext import commands
import random
import string

class Password(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def password(self, ctx, length: int = 12):
        if length < 6 or length > 64:
            return await ctx.send("❌ Longueur entre 6 et 64.")

        chars = string.ascii_letters + string.digits + "!@#$%^&*()"

        password = "".join(random.choice(chars) for _ in range(length))

        await ctx.author.send(f"🔐 Ton mot de passe : `{password}`")
        await ctx.send("📩 Mot de passe envoyé en DM.")

async def setup(bot):
    await bot.add_cog(Password(bot))