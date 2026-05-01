from discord.ext import commands
import time

class AntiSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.users = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        user_id = message.author.id
        now = time.time()

        if user_id not in self.users:
            self.users[user_id] = []

        self.users[user_id].append(now)

        # garde seulement les 5 derniers messages
        self.users[user_id] = self.users[user_id][-5:]

        # si 5 messages en moins de 3 secondes
        if len(self.users[user_id]) == 5 and now - self.users[user_id][0] < 3:
            try:
                await message.channel.send(f"🚫 {message.author.mention} spam détecté !")
                await message.delete()
            except:
                pass

async def setup(bot):
    await bot.add_cog(AntiSpam(bot))