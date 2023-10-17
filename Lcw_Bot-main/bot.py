import discord
import json
from discord.ext import commands
import random
import asyncio

intents=discord.Intents.all()
intents.typing=True
intents.presences=True
intents.members=True
intents.message_content=True
# client = discord.Client()
# client = discord.Client(intents=intents)
import os

with open('setting.json',mode='r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('>>Bot is online<<')

# @bot.event
# async def on_member_join(member):
#     channel=bot.get_channel(jdata['Welcome_channel'])
#     await channel.send(f"{member} join!")

# @bot.event
# async def on_member_remove(member):
#     channel=bot.get_channel(jdata['Leave_channel'])
#     await channel.send(f"{member} leave!")

# @bot.command()
# async def ping(ctx):
#     await ctx.send(f'{round(bot.latency*1000)}(ms)')

# @bot.command()
# async def 圖片(ctx):
#     random_pic=random.choice(jdata['pic'])
#     pic=discord.File(random_pic)
#     await ctx.send(file=pic)

# @bot.command()
# async def em(ctx):
#     embed=discord.Embed(title="About", description="About the bot")
#     embed.set_author(name="Lcw")
#     embed.add_field(name="1", value="11", inline=False)
#     embed.add_field(name="2", value="22", inline=False)
#     embed.add_field(name="3", value="33", inline=False)
#     embed.add_field(name="4", value="44", inline=False)
#     embed.set_footer(text="222")
#     await ctx.send(embed=embed)

# @bot.event
# async def on_message(msg):
#     keyword=jdata['keyword']
#     if msg.content in keyword and msg.author!=bot.user:
#         await msg.channel.send('hello')

@bot.command()
async def load(ctx,extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f'Loaded {extension} done.')


@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f'Un-Loaded {extension} done.')


@bot.command()
async def reload(ctx,extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f'Re-Loaded {extension} done.')

async def load_extensions():
    for Filename in os.listdir('./cmds'):
        if Filename.endswith('.py'):
            await bot.load_extension(f"cmds.{Filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(jdata['TOKEN'])   

if __name__=='__main__':
    asyncio.run(main())
