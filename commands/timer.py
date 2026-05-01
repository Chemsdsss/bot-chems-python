import asyncio

@bot.command()
async def timer(ctx, seconds: int):
    await ctx.send(f"⏱️ Timer lancé : {seconds} secondes")

    await asyncio.sleep(seconds)

    await ctx.send(f"⏰ {ctx.author.mention} ton timer est terminé !")