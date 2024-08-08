from alice.framework.commands.commandwrapper import CommandWrapper

class CommandFactory:
    """
    A class to generate commands that can easily be attached to the client.
    """

    @staticmethod
    def command(name_arg, command_function_arg):
        """
        Generate a static Command class with the provided name and command function.

        :param name_arg: String representing the command name.
        :param command_function_arg: Function to use for command callback.
        :return: Class of type CommandWrapper with the provided specifications.
        """
        
        class Command(CommandWrapper):
            name = name_arg
            command_function = command_function_arg
        return Command