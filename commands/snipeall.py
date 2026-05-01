import discord
from discord.ext import commands
import datetime

# =====================
# MEMORY STORAGE
# =====================
snipes = {}  # guild_id -> list of deleted messages


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class SnipeAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # =====================
    # SAVE DELETED MESSAGE
    # =====================
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        if not message.guild:
            return

        data = {
            "content": message.content if message.content else "[MEDIA]",
            "author": str(message.author),
            "channel": message.channel.name,
            "time": now()
        }

        guild_id = message.guild.id

        if guild_id not in snipes:
            snipes[guild_id] = []

        snipes[guild_id].append(data)

        # garder seulement les 50 derniers messages
        if len(snipes[guild_id]) > 50:
            snipes[guild_id].pop(0)

    # =====================
    # +SNIPE (dernier message salon)
    # =====================
    @commands.command()
    async def snipe(self, ctx):
        guild_id = ctx.guild.id

        if guild_id not in snipes or len(snipes[guild_id]) == 0:
            return await ctx.send("❌ Aucun message supprimé.")

        last = snipes[guild_id][-1]

        embed = discord.Embed(
            title="📌 Snipe",
            color=discord.Color.blue()
        )
        embed.add_field(name="Auteur", value=last["author"], inline=False)
        embed.add_field(name="Salon", value=last["channel"], inline=False)
        embed.add_field(name="Message", value=last["content"], inline=False)
        embed.set_footer(text=f"Heure: {last['time']}")

        await ctx.send(embed=embed)

    # =====================
    # +SNIPEALL (tout serveur)
    # =====================
    @commands.command()
    async def snipeall(self, ctx):
        guild_id = ctx.guild.id

        if guild_id not in snipes or len(snipes[guild_id]) == 0:
            return await ctx.send("❌ Aucun message supprimé.")

        embed = discord.Embed(
            title="📋 Snipe All (dernier messages)",
            color=discord.Color.red()
        )

        # afficher les 5 derniers
        for msg in snipes[guild_id][-5:]:
            embed.add_field(
                name=f"{msg['author']} | #{msg['channel']}",
                value=f"{msg['content']} ({msg['time']})",
                inline=False
            )

        await ctx.send(embed=embed)


# =====================
# SETUP
# =====================
async def setup(bot):
    await bot.add_cog(SnipeAll(bot))