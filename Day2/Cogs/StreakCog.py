from discord.ext import commands, tasks
import os
import json
from datetime import date, timedelta

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
        with open('../DiscordSettings/Data.json', 'r+') as f:
            people = json.load(f)
            if ctx.user in people and date(people[ctx.user]['history'][-1]) == date.strftime() + timedelta(days=1):
                people[ctx.user]['streak'] = people[ctx.user]['streak'] + 1
                people[ctx.user]['history'].append(date.strftime())
            else:
                people[ctx.user] = {'streak':0, 'history':[date.strftime()]}


    @commands.command()
    async def set_channel(self, ctx):
        # Sets whatever channel this command was called in the default place to post steam sales
        with open('../DiscordSettings/SteamScraperSettings.json', 'r+') as f:
            channel_dict = json.load(f)
            channel_dict[ctx.guild] = ctx.channel
            f.seek(0)
            json.dump(channel_dict, f)
            f.truncate()





def setup(client):
    client.add_cog(StreakCog(client))