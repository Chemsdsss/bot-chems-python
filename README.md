

# 🤖 Bot Chems — Discord Bot Multi-Fonctions

**Bot Chems** est un bot Discord complet développé en Python avec `discord.py`, conçu pour offrir une expérience riche à la communauté. Il embarque plus de **130 commandes** organisées en modules indépendants (système de Cogs), couvrant la modération, l'économie, les jeux, la musique, l'IA conversationnelle et bien plus encore.

---

## ✨ Fonctionnalités

### 🛡️ Modération
Kick, ban, unban, mute, unmute, warn, tempban, softban, lock/unlock de salons, slowmode, nuke, banlist, gestion des avertissements.

### 💰 Économie
Système de monnaie virtuelle avec balance, daily reward, pay, shop, buy, sell, inventaire, profil, leaderboard et gamble.

### 🎵 Musique

Lecture audio en vocal avec play, pause, resume, skip, stop, queue, nowplaying, volume et loop.

### 🤖 IA Conversationnelle
Commande `+ai` propulsée par **OpenRouter (GPT-3.5-turbo)** avec mémoire de conversation par utilisateur et persona personnalisée. Supporte le reset de mémoire (`+resetai`).

### 🎉 Giveaways & Événements
Création, gestion et reroll de giveaways, système de sondages (poll/endpoll), countdown, vote.

### 🔒 Sécurité Serveur
Anti-raid, anti-bot, anti-spam intégrés et configurables.

### 🎲 Fun & Divertissement
8ball, coinflip, dice, roll, iq, gay, pp, joke, meme, fakehack, hack, love, ship, couple, compatibilité, hug, slap, kiss, cuddle, punch.

### 🛠️ Utilitaires
Avatar, banner, userinfo, serverinfo, botinfo, snipe, editsnipe, embed, say, translate, calculator, calc, timer, remind, uptime, afk, dm, massdm, password, genpassword, invite, ascii, bigtext, smalltext, fliptext, reverse, rank, level, logs, modlogs.

### ⚙️ Configuration
Préfixe personnalisable (`+setprefix`), gestion des rôles (addrole, giverole, removerole, takerole), gestion des pseudos, configuration générale via `config.json`.

---

## 📁 Structure du projet

```
bot/
├── main.py              # Point d'entrée, chargement des Cogs
├── config.json          # Configuration (token, prefix, owners, presence...)
├── requirements.txt     # Dépendances Python
└── commands/            # Modules (un fichier = une commande)
    ├── ai.py
    ├── ban.py
    ├── economy.py
    ├── music.py
    └── ...              # +130 commandes
```

---

## 🚀 Installation

```bash
git clone https://github.com/ton-user/bot-chems.git
cd bot-chems
pip install -r requirements.txt
```

Configure `config.json` :
```json
{
  "token": "TON_TOKEN_DISCORD",
  "prefix": "+",
  "openrouter_api_key": "TA_CLE_OPENROUTER"
}
```

Lance le bot :
```bash
python main.py
```

---

## 🔧 Prérequis

- Python 3.10+
- discord.py >= 2.4.0
- Un token Discord ([discord.dev](https://discord.dev))
- Une clé API OpenRouter (pour la commande `+ai`)

---

## 📜 Commande principale

| Commande | Description |
|----------|-------------|
| `+aide`  | Affiche la liste de toutes les commandes |
| `+ai <message>` | Parle à l'IA avec mémoire de contexte |
| `+help` | Aide paginée |

---

## 👑 Crédits

Développé par **Chems** · Bot Discord personnel multi-fonctions.
