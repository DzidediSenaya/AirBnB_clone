#!/usr/bin/python3
"""
Command interpreter entry point.
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class.

    This class defines a command-line interpreter for interacting with the
    data storage of an AirBnB-like application.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at end of file (Ctrl+D).

        Usage: Ctrl+D
        """
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """
        Override to not execute anything on an empty line.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
