from discord.ext import commands
from alice.framework.commands.commandwrapper import CommandWrapper

@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")

class PingCommand(CommandWrapper):

    def __init__(self):
        super().__init__("ping", ping)