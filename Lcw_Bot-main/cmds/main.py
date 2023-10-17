import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    @commands.command()  #ctx:context(上下文)
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    # @commands.command()
    # async def hi(self,ctx):
    #     await ctx.send('ABCD')

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)



    
async def setup(bot):
    await bot.add_cog(Main(bot))
       