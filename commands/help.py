import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="aide")
    async def aide(self, ctx):
        commands_list = [
            c for c in self.bot.commands
            if not c.hidden
        ]

        per_page = 10
        pages = [commands_list[i:i + per_page] for i in range(0, len(commands_list), per_page)]

        for index, page in enumerate(pages):

            embed = discord.Embed(
                title=f"🤖 Aide du bot (Page {index + 1}/{len(pages)})",
                color=0x3498db
            )

            for command in page:
                name = f"`{self.bot.command_prefix}{command.name}`"
                desc = command.help or "Aucune description"

                embed.add_field(
                    name=name,
                    value=desc,
                    inline=False
                )

            embed.set_footer(text="Bot IA • COGS System")

            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))