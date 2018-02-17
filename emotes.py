import discord
from discord.ext import commands

class EmotesCog:
    '''Whole Bunch of Twitch Emotes'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, pass_context=True)
    async def tfw(self, ctx):
        await self.bot.send_file(ctx.message.channel, "basic_assets/pepe.jpg", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def kappa(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/kappa.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def kappahd(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/kappahd.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def pogchamp(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/pogchamp.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def kreygasm(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/krey.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def wutface(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel,"basic_assets/wutface.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def frankerz(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/frankerz.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def dansgame(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/dansgame.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def trihard(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/trihard.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def fourhead(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/4head.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def heyguys(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/heyguys.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def catbag(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/catbag.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def itsboshytime(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/boshy.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def vineface(self, ctx):
        """Emote."""
        await self.bot.send_file(ctx.message.channel, "basic_assets/vineface.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def no_more(self, ctx):
        await self.bot.send_file(ctx.message.channel, "basic_assets/nomore.png", filename = None)

    @commands.command(hidden=True, pass_context=True)
    async def rip(self, ctx):
        await self.bot.send_file(ctx.message.channel, "basic_assets/in_memory.jpg", filename = None)

def setup(bot):
    bot.add_cog(EmotesCog(bot))
