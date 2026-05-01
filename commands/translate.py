from googletrans import Translator

translator = Translator()

@bot.command()
async def translate(ctx, lang, *, text):
    result = translator.translate(text, dest=lang)
    await ctx.send(f"🌍 {result.text}")