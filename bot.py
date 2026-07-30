import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен!")


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="беседка")
    if channel:
        await channel.send(
            f"👋 Добро пожаловать, {member.mention}!\n\n"
            f"Я — **Михал Палыч Терентьев**, секретарь этого уважаемого гольф-клуба.\n"
            f"Располагайтесь."
        )


@bot.command()
async def помощь(ctx):
    await ctx.send(
        "**Команды:**\n"
        "`!помощь` — показать команды\n"
        "`!монетка` — подбросить монетку\n"
        "`!кубик` — бросить кубик"
    )


@bot.command()
async def монетка(ctx):
    await ctx.send(random.choice(["🟢 Орёл", "🔴 Решка"]))


@bot.command()
async def кубик(ctx):
    await ctx.send(f"🎲 Выпало: {random.randint(1,6)}")


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
