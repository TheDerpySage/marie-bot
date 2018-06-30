import discord
from discord.ext import commands
import urllib2
from ping3 import ping
import socket

def string_ping(host):
    response = ping(host)
    if response == None:
        return (host + " is unreachable.")
    else:
        return (host + " is reachable. (%sms)" % round(response * 1000))

def bool_ping(host):
    response = ping(host)
    if response == None:
        return False
    else:
        return True

def socket_test(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp = sock.connect_ex((host, port))
    if temp == 0: sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    return temp

class ServerCog:
    '''Server functions'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def current_ip(self, ctx):
        """Returns Current Public IP"""
        curIP = urllib2.urlopen('http://ip.42.pl/raw').read()
        await self.bot.say(curIP)

    @commands.command(pass_context = True)
    async def services(self, ctx):
        """Service Status"""
        await self.bot.send_typing(ctx.message.channel)
        #Check Toad-Town
        result = socket_test('192.168.0.13',80)
        if result == 0:
            toadHealth = ":white_check_mark:"
            public = True
        else:
            toadHealth = ":no_entry:(%s)" % result
            public = False
        #Check Web
        result = socket_test('192.168.0.8',80)
        if result == 0:
            webHealth = ":white_check_mark:"
            if public == False:
                webHealth = ":warning:"
        else: webHealth = ":no_entry:(%s)" % result
        #Check Plex
        result = socket_test('192.168.0.8',32400)
        if result == 0:
            plexHealth = ":white_check_mark:"
        else: plexHealth = ":no_entry:(%s)" % result
        #Check TF2
        result = socket_test('192.168.0.8',27015)
        if result == 0:
            tfHealth = ":white_check_mark:"
            sock.shutdown(socket.SHUT_RDWR)
        else: tfHealth = ":no_entry:(%s)" % result
        #Check Minecraft
        result = socket_test('45.55.104.100',25565)
        if result == 0:
            mineHealth = ":white_check_mark:"
        else: mineHealth = ":no_entry:(%s)" % result
        #Check Flower-Fields
        result = socket_test('192.168.0.12',80)
        if result == 0:
            flowerHealth = ":white_check_mark:"
            if public == False:
                flowerHealth=":warning:"
        else: flowerHealth = ":no_entry:(%s)" % result
        #Check Poshley-Heights
        result = socket_test('192.168.0.8',8083)
        if result == 0:
            poshHealth = ":white_check_mark:"
            if public == False:
                poshHealth = ":warning:"
        else: poshHealth = ":no_entry:(%s)" % result
        #Output
        temp = ("**SERVICES**" +
        "\n\n~Website~ " + "\nStatus:\t" + webHealth + "\nhttp://www.thederpysage.com/" +
        "\n\n~Plex~" + "\nStatus:\t" + plexHealth + "\n*Use their Website*" +
        "\n\n~Poshley Heights~" + "\nStatus:\t" + poshHealth + "\nhttp://poshley-heights.thederpysage.com/" +
        "\n\n~Flower Fields~" + "\nStatus:\t" + flowerHealth + "\n*Invite Only*" +
        "\n\n~Toad Town~" + "\nStatus:\t" + toadHealth + "\n*Reverse Proxy*" +
        "\n\n~Team Fortress 2 / Garry's Mod~" + "\nStatus:\t" + tfHealth + "\nsrc.thederpysage.com" +
        "\n\n~Minecraft~" + "\nStatus:\t" + mineHealth + "\n45.55.104.100:25565")
        await self.bot.say(temp)

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
        temp = ("**SERVERS**" +
        "\nNagato:\t" + nagato +
        "\nHatsuharu:\t" + hatsuharu +
        "\nShimakaze:\t" + shimakaze +
        "\nMutsu:\t" + mutsu)
        await self.bot.say(temp)

    @commands.command(aliases=['ping'], pass_context = True)
    async def bot_ping(self, ctx, hostname):
        """Pings a given host to check if it's reachable"""
        await self.bot.send_typing(ctx.message.channel)
        await self.bot.say(string_ping(hostname))


def setup(bot):
    bot.add_cog(ServerCog(bot))
