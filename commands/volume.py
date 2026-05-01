@bot.command()
async def volume(ctx, value: int):
    if value < 0 or value > 100:
        return await ctx.send("⚠️ Volume entre 0 et 100")

    await ctx.send(f"🔊 Volume réglé à {value}%")