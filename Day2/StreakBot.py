import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')
recent = None


@client.command()
async def rr(ctx):
    global recent
    await reload(ctx, recent)


@client.command()
async def load(ctx, extension):
    global recent
    recent = extension
    client.load_extension(f'cogs.{extension}')
    try:
        await ctx.send(f'{extension} loaded successfully')
    except Exception as e:
        await ctx.send(e)


@client.command()
async def unload(ctx, extension):
    global recent
    recent = extension
    client.unload_extension(f'cogs.{extension}')
    try:
        await ctx.send(f'{extension} unloaded successfully')
    except Exception as e:
        await ctx.send(e)


@client.command()
async def reload(ctx, extension):
    global recent
    recent = extension
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    try:
        await ctx.send(f'{extension} reloaded successfully')
    except Exception as e:
        await ctx.send(e)


@client.command()
async def reload_all(ctx):
    for filename in os.listdir('cogs'):
        try:
            client.unload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'{filename[:-3]} unloaded successfully')
        except Exception as e:
            await ctx.send(e)
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'{filename[:-3]} loaded successfully')
        except Exception as e:
            await ctx.send(e)

@client.command()
async def reload_folder(ctx, folder):
    for filename in os.listdir('./' + folder):
        try:
            client.unload_extension(f'{folder}.{filename[:-3]}')
            await ctx.send(f'folder unloaded')
        except Exception as e:
            await ctx.send(e)
        try:
            client.load_extension(f'{folder}.{filename[:-3]}')
            await ctx.send(f'folder loaded')
        except Exception as e:
            await ctx.send(e)


#  Inital loadings

with open('./DiscordSettings/CogLoad.txt', 'r') as f:
    for line in f:
        folder = line.strip('\n')
        for filename in os.listdir(f'./{folder}'):
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'{folder}.{filename[:-3]}')
                except Exception as e:
                    print(e)

with open('./DiscordSettings/token.txt', 'r') as token:
    client.run(token.read())