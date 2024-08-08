from discord.ext import commands
from alice.framework.commands.commandwrapper import CommandWrapper

@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")

class PingCommand(CommandWrapper):

    name = "ping"
    command_function = ping