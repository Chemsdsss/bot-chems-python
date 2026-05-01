import asyncio

@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, member: discord.Member, time: int, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"⛔ {member} ban pendant {time} secondes")

    await asyncio.sleep(time)

    await ctx.guild.unban(member)
    await ctx.send(f"✅ {member} a été unban")