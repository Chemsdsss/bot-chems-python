from discord.ext import commands
import random
import string

class Password(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def password(self, ctx, length: int = 12):
        chars = string.ascii_letters + string.digits + "!@#$%"

        pwd = "".join(random.choice(chars) for _ in range(length))

        await ctx.author.send(f"🔐 {pwd}")
        await ctx.send("📩 Envoyé en DM")

async def setup(bot):
    await bot.add_cog(Password(bot))