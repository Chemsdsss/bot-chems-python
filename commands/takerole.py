@bot.command()
@commands.has_permissions(manage_roles=True)
async def takerole(ctx, member: discord.Member, role: discord.Role):
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send(f"❌ Rôle **{role.name}** retiré à {member.mention}")
    else:
        await ctx.send("⚠️ Ce membre n’a pas ce rôle.")