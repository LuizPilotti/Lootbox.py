# pip install discord.py

import discord
import random
from discord.ext import commands

# Configurações iniciais do bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Definindo os itens da lootbox com raridades
lootbox_items = [
    {"name": "Espada Lendária", "rarity": "Lendário", "chance": 1},
    {"name": "Escudo Raro", "rarity": "Raro", "chance": 10},
    {"name": "Poção Comum", "rarity": "Comum", "chance": 50},
    {"name": "Cristal Épico", "rarity": "Épico", "chance": 5},
    {"name": "Anel Incomum", "rarity": "Incomum", "chance": 20},
]


# Função para sortear o item da lootbox
def abrir_lootbox():
    total_chance = sum(item["chance"] for item in lootbox_items)
    sorteio = random.randint(1, total_chance)
    acumulado = 0

    for item in lootbox_items:
        acumulado += item["chance"]
        if sorteio <= acumulado:
            return item
    return None


# Comando de lootbox no Discord
@bot.command(name="lootbox")
async def lootbox(ctx):
    item = abrir_lootbox()
    if item:
        await ctx.send(f"🎉 {ctx.author.mention} você recebeu: **{item['name']}**! (Raridade: {item['rarity']})")
    else:
        await ctx.send("❌ Algo deu errado ao abrir a lootbox.")


# Função de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online e pronto para uso!')


# Insira o token do bot aqui
bot.run("SEU_TOKEN_AQUI")
