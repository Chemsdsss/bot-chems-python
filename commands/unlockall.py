@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel

    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True

    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"🔓 {channel.mention} est maintenant ouvert")