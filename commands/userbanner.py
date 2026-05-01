@bot.command()
async def userbanner(ctx, member: discord.Member = None):
    member = member or ctx.author

    user = await bot.fetch_user(member.id)
    if user.banner:
        await ctx.send(user.banner.url)
    else:
        await ctx.send("❌ Aucun banner trouvé")