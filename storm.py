import discord
from discord.ext import commands
from weather import Weather, Unit #weather-api

class StormCog:
    '''For Important Weather Alert Parsing'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['weather'], pass_context=True)
    async def current(self, ctx, *, givenLocation : str = None):
        """Gets the current weather of a specified location (by default it looks up Ames and Des Moines)."""
        nws = Weather(unit=Unit.FAHRENHEIT)
        if(givenLocation == None):
            location = nws.lookup_by_location('ames, iowa')
            condition = location.condition
            result = (location.description[7:] + '\n' +
            'Currently:\t' + condition.text + ', ' + condition.temp + "°F\n\n")
            location = nws.lookup_by_location('des moines, iowa')
            condition = location.condition
            result = (result + location.description[7:] + '\n' +
            'Currently:\t' + condition.text + ', ' + condition.temp + "°F")
        else:
            location = nws.lookup_by_location(givenLocation)
            condition = location.condition
            result = (location.description[7:] + '\n' +
            'Currently:\t' + condition.text + ', ' + condition.temp + "°F")
        await self.bot.say(result)

    # Day forecast command possibly coming soon

def setup(bot):
    bot.add_cog(StormCog(bot))
