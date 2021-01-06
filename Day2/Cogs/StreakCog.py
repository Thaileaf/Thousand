from discord.ext import commands, tasks
import os
import json
from datetime import datetime, timedelta

class StreakCog(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        # Prints message when cog is online
        print('Streak Cog Ready')
        # self.post_steam_sale.start()

    @commands.command()
    async def streak(self, ctx):
        # Adds one day to streak and records date
        if not os.path.exists('./DiscordSettings/Data.json'):
            with open('./DiscordSettings/Data.json', 'w+') as f:
                json_object = json.dumps({})
                f.write(json_object)
        with open('./DiscordSettings/Data.json', 'r') as f:
            people = json.load(f)
            if ctx.message.author.id in people and datetime(people[ctx.message.author.id]['history'][-1]) == datetime.now() + timedelta(days=1):
                people[ctx.message.author.id]['streak'] = people[ctx.message.author.id]['streak'] + 1
                people[ctx.message.author.id]['history'].append(datetime.now())
            else:
                print(people)
                people[ctx.message.author.id] = {'streak':0, 'history':[datetime.now().strftime("%Y-%d-%m %H:%M:%S")]}
                print(people)
        with open('./DiscordSettings/Data.json', 'w') as f:
            json.dump(people, f, indent=4)






    @commands.command()
    async def set_channel(self, ctx):
        # Sets whatever channel this command was called in the default place to post steam sales
        with open('./DiscordSettings/SteamScraperSettings.json', 'r+') as f:
            channel_dict = json.load(f)
            channel_dict[ctx.guild] = ctx.channel
            f.seek(0)
            json.dump(channel_dict, f)
            f.truncate()

    @commands.command()
    async def find_dir(self, ctx):
        print(os.getcwd())
        os.chdir('..')
        print(os.getcwd())





def setup(client):
    client.add_cog(StreakCog(client))