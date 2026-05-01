from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: commands.MemberConverter = None):
        member = member or ctx.author

        embed = {
            "title": f"Infos sur {member}",
            "description": f"ID: {member.id}",
            "fields": [
                {"name": "Compte créé le", "value": str(member.created_at)[:19]},
                {"name": "A rejoint le", "value": str(member.joined_at)[:19]}
            ]
        }

        await ctx.send(
            f"👤 **{member}**\n"
            f"ID: {member.id}\n"
            f"Créé le: {str(member.created_at)[:19]}\n"
            f"Rejoint le: {str(member.joined_at)[:19]}"
        )

async def setup(bot):
    await bot.add_cog(UserInfo(bot))