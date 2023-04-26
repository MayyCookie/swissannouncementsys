import discord
from discord.ext import commands

class HostPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def host(self, ctx):
        await ctx.send("What is the time of the flight?")
        flight_time = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        await ctx.send("What is the time of departure?")
        departure_time = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        await ctx.send("Thank you! Announcing in the channel...")
        announcement = f"Flight at {flight_time.content} departing at {departure_time.content}."
        channel = self.bot.get_channel(991475748756009014)
        await channel.send(announcement)
        
def setup(bot):
    bot.add_cog(HostPlugin(bot))
