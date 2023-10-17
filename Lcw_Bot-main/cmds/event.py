import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json',mode='r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel=self.bot.get_channel(jdata['Welcome_channel'])
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(jdata['Leave_channel'])
        await channel.send(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword=jdata['keyword']
        if msg.content in keyword and msg.author!=self.bot.user:
            await msg.channel.send('hello')

    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="About", description="About the bot")
        embed.set_author(name="Lcw")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=False)
        embed.add_field(name="3", value="33", inline=False)
        embed.add_field(name="4", value="44", inline=False)
        embed.set_footer(text="222")
        await ctx.send(embed=embed)
        

async def setup(bot):
    await bot.add_cog(Event(bot))