from discord.ext import commands
from alice.framework.commands.commandwrapper import CommandWrapper

@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")

class PingCommand(CommandWrapper):
    """
    Simple Command to respond to a simple invoked command.
    """

    name = "ping"
    command_function = ping