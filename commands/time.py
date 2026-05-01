from datetime import datetime

@bot.command()
async def time(ctx):
    now = datetime.now().strftime("%H:%M:%S")
    await ctx.send(f"🕒 Heure actuelle : {now}")