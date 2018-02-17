import discord
from discord.ext import commands

class AdminCog:
	'''Majora/Server Owner Only stuff'''

	def __init__(self, bot):
		self.bot = bot
		self.AppInfo = bot.application_info()

	@commands.command(hidden=True, pass_context=True)
	async def echo(self, ctx, *, message: str):
		if(ctx.message.author == ctx.message.server.owner):
			await self.bot.say(message)
		else : await self.bot.say("Nah.")

	@commands.command(hidden=True, pass_context=True)
	async def reset(self, ctx):
		if(ctx.message.author == ctx.message.server.owner):
			await self.bot.say(":0 Ok! Hold on one second.")
			exit()
		await self.bot.say("No.")

	@commands.command(hidden=True, pass_context=True)
	async def sign_off(self, ctx):
		if(ctx.message.author == ctx.message.server.owner):
			await self.bot.say("https://www.youtube.com/watch?v=aDrUQftLsz8")
			await self.bot.say("Bye now!")
			exit()

	@commands.command()
	async def credits(self):
		'''Show credits.'''
		await bot.say("`Marie Server Bot created by TheDerpySage.`")
		await bot.say("`Questions/Concerns? Add via Discord`")
		await bot.say("`@TheDerpySage#2049`")

def setup(bot):
	bot.add_cog(AdminCog(bot))
