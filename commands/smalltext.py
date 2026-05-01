@bot.command()
async def smalltext(ctx, *, text):
    normal = "abcdefghijklmnopqrstuvwxyz"
    small = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ"

    result = ""
    for char in text.lower():
        if char in normal:
            result += small[normal.index(char)]
        else:
            result += char

    await ctx.send(result)