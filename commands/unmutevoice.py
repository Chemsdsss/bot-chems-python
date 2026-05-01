@bot.command()
@commands.has_permissions(mute_members=True)
async def unmutevoice(ctx, member: discord.Member):
    await member.edit(mute=False)
    await ctx.send(f"🔊 {member.mention} n’est plus mute vocal")