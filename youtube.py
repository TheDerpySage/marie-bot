import discord
from discord.ext import commands
import random
#HTML Scraping
import urllib.request
from bs4 import BeautifulSoup

class YoutubeCog:
    '''Video related stuff'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def boy_next_door(self):
        """The Bot will show you some of it's favorite videos."""
        random.seed()
        x = random.randint(1,3)
        if x == 1:
            await self.bot.say("https://www.youtube.com/watch?v=T3iHxLs5maM")
        elif x == 2:
            await self.bot.say("https://www.youtube.com/watch?v=qPJvGMYxDPs")
        elif x >= 3:
            await self.bot.say("https://www.youtube.com/watch?v=JhH1waXoHy8")

    @commands.command(hidden=True)
    async def go_to_bed(self):
        """But you can go to bed."""
        random.seed()
        x = random.randint(1,3)
        if x == 1:
            await self.bot.say("https://www.youtube.com/watch?v=NeO1PxwEr8Q")
        elif x == 2:
            await self.bot.say("https://www.youtube.com/watch?v=kNnwzB61Wc8")
        elif x == 3:
            await self.bot.say("https://www.youtube.com/watch?v=EOVy3HEMjmU")
        elif x >= 4:
            await self.bot.say("https://www.youtube.com/watch?v=k8stXdjRkSI")

    @commands.command(pass_context=True)
    async def youtube(self, ctx, *, search : str = None):
        """Searches youtube and gives you the first result"""
        await self.bot.send_typing(ctx.message.channel)
        if search is None:
            search = "https://www.youtube.com/watch?v=KMU0tzLwhbE"
        url = "https://www.youtube.com/results?search_query=" + search.strip().replace(" ", "+") + "&sp=EgIQAQ%253D%253D"
        html = urllib.request.urlopen(urllib.request.Request(url)).read()
        soup = BeautifulSoup(html, "html.parser")
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            #The If below filters out advertisement responses
            if "https://googleads" not in vid['href']:
                await self.bot.say('https://www.youtube.com' + vid['href'])
                break

def setup(bot):
    bot.add_cog(YoutubeCog(bot))
