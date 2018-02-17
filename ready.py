import discord
from discord.ext import commands

#Ready up cog concept made for HLPugs
#By @TheDerpySage#2049

class ReadyCog:
    '''Ready Up Proof of Concept'''

    def __init__(self, bot):
        self.bot = bot
        #Edit this line with the name of the role
        #The role should A) exist and B) be mentionable
        self.role_name = "Ready"

    @commands.command(pass_context=True)
    async def ready_up(self, ctx):
        """Ready up."""
        try:
            role = discord.utils.get(ctx.message.server.roles, name=self.role_name)
            try:
                await self.bot.add_roles(ctx.message.author, role)
                await self.bot.say(ctx.message.author.name + " is ready!")
            except discord.Forbidden:
                await self.bot.say("I don't have permission to mess with roles!")
        except:
            await self.bot.say("No such role. Maybe you forgot to edit the file?")

    @commands.command(pass_context=True)
    async def unready(self, ctx):
        """Unready."""
        try:
            role = discord.utils.get(ctx.message.server.roles, name=self.role_name)
            try:
                await self.bot.remove_roles(ctx.message.author, role)
                await self.bot.say(ctx.message.author.name + " has unreadied.")
            except discord.Forbidden:
                await self.bot.say("I don't have permission to mess with roles!")
        except:
            await self.bot.say("No such role. Maybe you forgot to edit the file?")

    @commands.command(pass_context=True)
    async def notify(self, ctx):
        """Notify ready users (admin only)."""
        try:
            role = discord.utils.get(ctx.message.server.roles, name=self.role_name)
            if(ctx.message.author == ctx.message.server.owner or discord.AppInfo.owner):
                await self.bot.say(role.mention + " it is time!")
            else: await self.bot.say("Nah.")
        except:
            await self.bot.say("No such role. Maybe you forgot to edit the file?")

def setup(bot):
    bot.add_cog(ReadyCog(bot))
