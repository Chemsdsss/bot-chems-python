warns = {}

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unwarn(ctx, member: discord.Member):
    if member.id not in warns or warns[member.id] == 0:
        return await ctx.send("⚠️ Aucun warn")

    warns[member.id] -= 1
    await ctx.send(f"✅ 1 warn retiré à {member.mention} (reste {warns[member.id]})")