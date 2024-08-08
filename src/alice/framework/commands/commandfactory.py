from alice.framework.commands.commandwrapper import CommandWrapper

class CommandFactory:

    def command(name_arg, command_function_arg):
        class Command(CommandWrapper):
            name = name_arg
            command_function = command_function_arg
        return Command