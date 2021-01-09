from discord.ext import commands, tasks
import os
import json
from datetime import datetime, timedelta
import math

class StreakCog(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        # Prints message when cog is online
        print('Streak Cog Ready')
        # Adds one day to streak and records date
        if not os.path.exists('./DiscordSettings/Data.json'):
            with open('./DiscordSettings/Data.json', 'w+') as f:
                json_object = json.dumps({})
                f.write(json_object)
        # self.post_steam_sale.start()

    @commands.command()
    async def streak(self, ctx):


        with open('./DiscordSettings/Data.json', 'r+') as f:
            people = json.load(f)
            id = str(ctx.message.author.id)


            if id in people:
                last_date = datetime.strptime(people[id]['history'][-1], '%Y-%m-%d %H:%M:%S').date()
                new_date = last_date + timedelta(days=1)
                cur = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if datetime.now().date() == new_date:
                    people[id]['streak'] = people[id]['streak'] + 1
                    streak = people[id]['streak']
                    history = people[id]['history']


                    history.append(cur)

                    await ctx.send(f'>>> Streak updated!\n{ctx.message.author.name}\nStreak: {streak}\nDate Saved: {history[-1]}')
                elif datetime.now().date() < new_date:
                    await ctx.send(f'>>> Too Soon. Try again tomorrow.')
                else:
                    await ctx.send(f'>>> Streak reset :(\n{ctx.message.author.name}\nStreak: 1\nDate Saved: {cur}')
                    people[id] = {'streak': 1, 'history': [cur]}
            else:
                cur = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                await ctx.send(f'>>> New Streak Started!\n{ctx.message.author.name}\nStreak: 1\nDate Saved: {cur}')
                people[id] = {'streak':1, 'history':[cur]}

            f.seek(0)
            json.dump(people, f, indent=4)
            f.truncate()

    @commands.command()
    async def view_streak(self, ctx, page=1):
        with open('./DiscordSettings/Data.json', 'r') as f:
            people = json.load(f)
            id = str(ctx.message.author.id)

            if id not in people:
                await ctx.send(">>> You're not in the system. Spooky.")
            else:
                history = people[id]['history']
                mx_pg = math.ceil(len(history) / 10)
                if mx_pg < page:
                    await ctx.send('>>> Invalid page no')
                else:
                    indices = (page - 1) * 10
                    history_txt = ''
                    for i in range(1 + indices,11 + indices):
                        try:
                            print(i)
                            history_txt = history_txt + history[-i] + '\n'
                        except Exception as e:
                            print(e)
                            break

                    await ctx.send(f">>> ```CSS\nCurrent streak at: {people[id]['streak']}\nHistory(Newest to Oldest):\n```\n{history_txt}\nPage {page}/{mx_pg} (view_streak [page_no] to change pages)")



    @commands.command()
    async def change_streak(self, ctx, new_streak):
        with open('./DiscordSettings/Data.json', 'r+') as f:
            people = json.load(f)
            id = str(ctx.message.author.id)

            if id in people:
                people[id]['streak'] = new_streak
                await ctx.send(f'>>> Streak changed to {new_streak}. Better not be cheating BUD')
            else:
                await ctx.send(">>> You're not in the system, BUD")


            f.seek(0)
            json.dump(people, f, indent=4)
            f.truncate()






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