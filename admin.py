import discord
from discord.ext import commands

class AdminCog:
	'''Majora/Server Owner Only stuff'''

	def __init__(self, bot):
		self.bot = bot

	# Self made check since is_owner() doesnt appear to be working and includes server owner
	# For Myself and the Server Owner
	def is_super(ctx):
		return (ctx.message.author.id == "89033229100683264") or (ctx.message.author == ctx.message.server.owner)

	@commands.command(hidden=True, pass_context=True)
	@commands.check(is_super)
	async def echo(self, ctx, *, message: str):
		await self.bot.say(message)

	@commands.command(name="reset", aliases=['restart'], hidden=True, pass_context=True)
	@commands.check(is_super)
	async def reset(self, ctx):
		await self.bot.say(":0 Ok! Hold on one second.")
		exit()

	@commands.command(hidden=True, pass_context=True)
	@commands.check(is_super)
	async def sign_off(self, ctx):
		await self.bot.say("https://www.youtube.com/watch?v=aDrUQftLsz8")
		await self.bot.say("Bye now!")
		exit()

	# Cog Management
	@commands.command(name='load', pass_context=True, hidden=True)
	@commands.check(is_super)
	async def cog_load(self, ctx, *, cog: str):
		"""Command which Loads a Module. Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.load_extension(cog)
		except Exception as e:
			await self.bot.say('**`ERROR: %s`**' % e)
		else:
			await self.bot.say('**`SUCCESS`**')

	@commands.command(name='unload', pass_context=True, hidden=True)
	@commands.check(is_super)
	async def cog_unload(self, ctx, *, cog: str):
		"""Command which Unloads a Module. Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			await self.bot.say('**`ERROR: %s`**' % e)
		else:
			await self.bot.say('**`SUCCESS`**')

	@commands.command(name='reload', pass_context=True, hidden=True)
	@commands.check(is_super)
	async def cog_reload(self, ctx, *, cog: str):
		"""Command which Reloads a Module. Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		except Exception as e:
			await self.bot.say('**`ERROR: %s`**' % e)
		else:
			await self.bot.say('**`SUCCESS`**')

	@commands.command()
	async def credits(self):
		'''Show credits.'''
		await bot.say("`Marie Server Bot created by TheDerpySage.`")
		await bot.say("`Questions/Concerns? Add via Discord`")
		await bot.say("`@TheDerpySage#2049`")

def setup(bot):
	bot.add_cog(AdminCog(bot))
