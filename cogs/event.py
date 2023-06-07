import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        activ = discord.Activity(type=discord.ActivityType.streaming, name='нифига, я жив?!!! (в разработке)', url='https://www.youtube.com/watch?v=4XMb_NeVUMA')
        await self.bot.change_presence(activity=activ, status=discord.Status.online)
        print('Я готов впахивать как (додумайте сами).')

    @Cog.listener()
    async def on_connect(self):
        print('Братан, я подключился к серверу.')

    @Cog.listener()
    async def on_disconnect(self):
        print('Меня отключили, батька помохи.')

    @Cog.listener()
    async def on_guild_remove(self, guild):
        print('Меня выгнали из {}. Помохи'.format(guild))

    @Cog.listener()
    async def on_guild_join(self, guild):
        print('Хто въехал в наш сервер?')    

    @Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user.display_name} запретили въезд на сервер')

    @Cog.listener()
    async def on_member_unban(self, guild, user):
        print(f'{user.username} разрешён въезд на сервер. Стоп, НЕПОНЯЛ, ВСМЫСЛЕ, КТО РАЗРЕШИЛ?!?!?!')

async def setup(bot):
    await bot.add_cog(Event(bot))