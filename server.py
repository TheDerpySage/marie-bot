import discord
from discord.ext import commands
import socket
#HTML Scraping
import urllib.request
from bs4 import BeautifulSoup
#Program Starting
import os

class ServerCog:
    '''Server functions'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def status(self, ctx):
        """Returns current IP and links to server applications"""
        await self.bot.send_typing(ctx.message.channel)
        #Check Public Facing IP
        html = urllib.request.urlopen(urllib.request.Request("http://ip.42.pl/raw")).read()
        soup = BeautifulSoup(html, "html.parser")
        curIP = soup.get_text()
        #Check Plex
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1',32400))
        if result == 0:
            plexHealth = "Active"
        else: plexHealth = "Inactive"
        #Check Web
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1',80))
        if result == 0:
            webHealth = "Active"
        else: webHealth = "Inactive"
        #Check TF2
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1',27015))
        if result == 0:
            tfHealth = "Active"
        else: tfHealth = "Inactive"
        #Check Minecraft
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1',25565))
        if result == 0:
            mineHealth = "Active"
        else: mineHealth = "Inactive"
        #Output
        await self.bot.say("Current IP:\t" + curIP +
        "\n\n~Webhost~ " + "\nStatus:\t" + webHealth + "\nPublic:\thttp://www.thederpysage.com/" +
        "\n\n~Plex~" + "\nStatus:\t" + plexHealth + "\nPublic:\thttp://www.thederpysage.com/plex/" + "\nInternal:\thttp://rogueport:32400/web/" +
        "\n\n~Team Fortress 2 / Garry's Mod~" + "\nStatus:\t" + tfHealth + "\nIP:\t" + curIP + ":27015" +
        "\n\n~Minecraft~" + "\nStatus:\t" + mineHealth + "\nIP:\t" + curIP + ":25565")

def setup(bot):
    bot.add_cog(ServerCog(bot))
