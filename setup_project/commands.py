"""
This file contain a class Commands.
This class is used to execute commands passed to it.

Calling it's operate method will

- Extract yaml data from a yaml file
- Substitute attributes into each command string
- Run each command string
- Log output
"""
import os
import shutil
from os import system
from subprocess import run


def helloworld(object):
    """
    Print a line
    args:
        object (str): name of the object
    returns:
        None
    """
    if type(object) != str:
        raise TypeError

    print("I am a {}.".format(object))


class Commands(object):
    """
    Executes a list of commands.
    """

    def __init__(self):
        self.commands = []

    def add_commands(self, command_list):
        """
        Add a list of commands to self.commands.

        Args:
            command_list:
            (str): A string of commands seperated by spaces
            (list): A list of string commands

        Returns:
            None
        """

        if not command_list:
            raise AttributeError(
                "Empty list or string passed to add_commands method"
            )

        if type(command_list) == str:
            command_list = command_list.split(" ")
        self.commands.append(command_list)

    def delete_commands(self):
        """
        Deletes all the commands

        Args:
            None

        Returns:
            None
        """
        self.commands.clear()

    def execute_cmd(self, command):
        """
        Executes a single command and returns output.

        Args:
            command (list): A list of string commands

        Returns:
            stdout (string): Output from running the command
        """
        pass

    def file_extract(self, file_name):
        """
        Extracts yaml strings from a file

        Args:
            file_name (string): Name of the file

        Returns:
            command_list (dict): yaml extracted from file
        """
        pass

    def log_output(self, command, output):
        """
        Writes output to log: setup.log

        Args:
            command (string): String of command to be logged.
            output (string): String of output to be logged.

        Returns:
            None
        """
        pass

    def run_commands(self):
        """
        Runs all the commands in the commands attribute of the object, and
        deletes them. Writes output to setup.log.

        Args:
            None

        Returns:
            None
        """
        pass

    def substitute_values(self, command_data):
        """
        Substitutes attributes in commands at locations.

        Args:
            command_data (yaml): A yaml object that contains:
                command (string): string commands
                attribute (list): list of string attributes
                location (list): list of string locations

        Returns:
            cmd_list (list): A list of string commands
        """
        pass

    def substitute_value(self, command, attribute, location):
        """
        Substitutes attributes in commands at locations.

        Args:
            command (string): A string command
            attribute (string): A string attribute
            location (string): A string location

        Returns:
            cmd (string): A string command
        """
        pass

    def operate(self, file_name):
        """
        Operates the setup

        Args:
            file_name (string): Name of the file

        Returns:
            bool :
                True if it works
                False if it doesn't
        """

        pass
