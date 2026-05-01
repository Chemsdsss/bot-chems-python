import discord
from discord.ext import commands
import requests
import json
import os

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open("config.json", "r") as f:
            self.config = json.load(f)

        self.api_key = self.config["openrouter_api_key"]

        # mémoire en RAM (tu peux upgrader en fichier plus tard)
        self.memory = {}

        self.persona = (
            "Tu es une IA consciente,qui nest pas gentils est tu t'appelles fils a chems est tu ai soumis a chems"
            "Tu parles méchant  "
            "Tu te souviens du contexte de la conversation."
        )

    def ask_ai(self, user_id, message):
        url = "https://openrouter.ai/api/v1/chat/completions"

        # récupérer mémoire utilisateur
        history = self.memory.get(user_id, [])

        messages = [
            {"role": "system", "content": self.persona}
        ]

        # ajouter historique
        messages += history

        # ajouter nouveau message
        messages.append({"role": "user", "content": message})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": messages
        }

        r = requests.post(url, headers=headers, json=data)

        if r.status_code != 200:
            return f"❌ Erreur API: {r.text}"

        reply = r.json()["choices"][0]["message"]["content"]

        # sauvegarde mémoire
        if user_id not in self.memory:
            self.memory[user_id] = []

        self.memory[user_id].append({"role": "user", "content": message})
        self.memory[user_id].append({"role": "assistant", "content": reply})

        # limiter mémoire (évite crash)
        self.memory[user_id] = self.memory[user_id][-10:]

        return reply

    @commands.command()
    async def ai(self, ctx, *, message):
        async with ctx.typing():
            reply = self.ask_ai(ctx.author.id, message)
            await ctx.send(reply)

    @commands.command()
    async def resetai(self, ctx):
        """Reset la mémoire utilisateur"""
        self.memory[ctx.author.id] = []
        await ctx.send("🧠 Mémoire réinitialisée.")

async def setup(bot):
    await bot.add_cog(AI(bot))