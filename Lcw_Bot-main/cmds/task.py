import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

with open('setting.json',mode='r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, bot):
        super().__init__(bot)

        self.counter=0

        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel=self.bot.get_channel(jdata['Task_channel'])
        #     while not self.bot.is_closed():
        #         await self.channel.send("Hi I'm running")
        #         await asyncio.sleep(5)
            
        # self.bg_task=self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(jdata['Task_channel'])
            while not self.bot.is_closed():
                now_time=datetime.datetime.now().strftime("%H%M")
                with open('setting.json',mode='r',encoding='utf-8') as jfile:
                    jdata=json.load(jfile)
                if str(now_time) == jdata['time'] and self.counter==0:
                    await self.channel.send("Hi dc")
                    self.counter=1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task=self.bot.loop.create_task(time_task())
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel=self.bot.get_channel(ch)
        await ctx.send(f"Set channel:{self.channel.mention}")   #mention=@

    @commands.command()
    async def set_time(self,ctx,time):
        with open('setting.json',mode='r',encoding='utf-8') as jfile:
            jdata=json.load(jfile)

        jdata['time']=time
        with open('setting.json',mode='w',encoding='utf-8') as jfile:
            json.dump(jdata,jfile,indent=4)

async def setup(bot):
    await bot.add_cog(Task(bot))