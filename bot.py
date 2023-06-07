from discord import Embed, Intents
from discord.ext import commands
import asyncio
import os
from json import load

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('config.json', 'r') as f:
    token = load(f).get('token')
    
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

bot.remove_command('help')

extension = None

@bot.command()
async def help(ctx):
    emb = Embed(title='Информация о командах (<обезательный параметр>, [необезательный параметр])', colour=0xffff00)
    emb.add_field(name='help', value='Показывает это сообщение.')
    emb.add_field(name='fox', value='Выдаёт случайное изоображение лисы.')
    emb.add_field(name='cat', value='Выдаёт случайное изоображение кота.')
    emb.add_field(name='rPand', value='Выдаёт случайное изоображение красной панды.')
    emb.add_field(name='ban <user> [reason]', value='Банит участников. (Только для людей разрешением)')
    emb.add_field(name='unban <user> [reason]', value='Разбанивает участников. (Только для людей разрешением)')
    emb.add_field(name='allClear', value='Чистит историю сообщений. (Только для людей разрешением)')
    emb.add_field(name='oauth_url <client_id>, [permission]', value='Выдаёт ссылку на приглашение для бота на сервер(только для одменов).')
    emb.add_field(name='usdRub', value='Выдаёт курс доллара к рублю.')
    emb.add_field(name='eurRub', value='Выдаёт курс евро к рублю.')
    emb.add_field(name='mBall', value='Просто Магический шар.')
    await ctx.send(embed=emb)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(token)

asyncio.run(main())
