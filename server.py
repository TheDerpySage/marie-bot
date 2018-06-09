import discord
from discord.ext import commands
#HTML Scraping
import urllib.request
from bs4 import BeautifulSoup
#Ping Tool
from ping3 import ping
import socket

def string_ping(host):
    response = ping(host)
    if response == None:
        return (host + " is unreachable.")
    else:
        return (host + " is reachable. (%sms)" % round(response, 2))

def bool_ping(host):
    response = ping(host)
    if response == None:
        return False
    else:
        return True

class ServerCog:
    '''Server functions'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def current_ip(self, ctx):
        """Returns Current Public IP"""
        await self.bot.send_typing(ctx.message.channel)
        html = urllib.request.urlopen(urllib.request.Request("http://ip.42.pl/raw")).read()
        soup = BeautifulSoup(html, "html.parser")
        curIP = soup.get_text()
        await self.bot.say(curIP)

    @commands.command(pass_context = True)
    async def services(self, ctx):
        """Service Status"""
        await self.bot.send_typing(ctx.message.channel)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Check Web
        result = sock.connect_ex(('192.168.0.8',80))
        if result == 0:
            webHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: webHealth = ":no_entry:(%s)" % result
        #Check Plex
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.8',32400))
        if result == 0:
            plexHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: plexHealth = ":no_entry:(%s)" % result
        #Check TF2
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.8',27015))
        if result == 0:
            tfHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: tfHealth = ":no_entry:(%s)" % result
        #Check Minecraft
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.8',25565))
        if result == 0:
            mineHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: mineHealth = ":no_entry:(%s)" % result
        #Check Toad-Town
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.13',80))
        if result == 0:
            toadHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: toadHealth = ":no_entry:(%s)" % result
        #Check Flower-Fields
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.12',80))
        if result == 0:
            flowerHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: flowerHealth = ":no_entry:(%s)" % result
        #Check Poshley-Heights
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.8',8083))
        if result == 0:
            poshHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: poshHealth = ":no_entry:(%s)" % result
        sock.close()
        #Output
        await self.bot.say("**SERVICES**" +
        "\n\n~Website~ " + "\nStatus:\t" + webHealth + "\nhttp://www.thederpysage.com/" +
        "\n\n~Plex~" + "\nStatus:\t" + plexHealth + "\nhttp://plex.thederpysage.com/web/" +
        "\n\n~Poshley Heights~" + "\nStatus:\t" + poshHealth + "\nhttp://poshley-heights.thederpysage.com/" +
        "\n\n~Flower Fields~" + "\nStatus:\t" + flowerHealth + "\n*Invite Only*" +
        "\n\n~Toad Town~" + "\nStatus:\t" + toadHealth + "\n*Reverse Proxy*" +
        "\n\n~Team Fortress 2 / Garry's Mod~" + "\nStatus:\t" + tfHealth + "\nsrc.thederpysage.com" +
        "\n\n~Minecraft~" + "\nStatus:\t" + mineHealth + "\nminecraft.thederpysage.com")

    @commands.command(pass_context = True)
    async def servers(self, ctx):
        """Server Status"""
        await self.bot.send_typing(ctx.message.channel)
        if bool_ping("nagato.home"):
            nagato = ":white_check_mark:"
        else : nagato = ":no_entry:"
        if bool_ping("hatsuharu.home"):
            hatsuharu = ":white_check_mark:"
        else : hatsuharu = ":no_entry:"
        if bool_ping("shimakaze.home"):
            shimakaze = ":white_check_mark:"
        else : shimakaze = ":no_entry:"
        await self.bot.say("**SERVERS**" +
        "\nNagato:\t" + nagato +
        "\nHatsuharu:\t" + hatsuharu +
        "\nShimakaze:\t" + shimakaze)

    @commands.command(pass_context = True)
    async def bot_ping(self, ctx, hostname):
        """Pings a given host to check if it's reachable"""
        self.bot.say(string_ping(hostname))

def setup(bot):
    bot.add_cog(ServerCog(bot))
