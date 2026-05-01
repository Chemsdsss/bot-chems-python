import time

start_time = time.time()

@bot.command()
async def uptime(ctx):
    seconds = int(time.time() - start_time)

    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60

    await ctx.send(f"⏱️ Uptime: {h}h {m}m {s}s")