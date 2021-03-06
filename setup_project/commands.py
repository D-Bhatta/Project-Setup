"""
This file contain a class Commands.
This class is used to execute commands passed to it.

Calling it's operate method will

- Extract yaml data from a yaml file
- Substitute attributes into each command string
- Run each command string
- Log output
"""
import logging
import logging.config
import os
import shutil
import subprocess
from json import load as jload
from os import system
from subprocess import run

import yaml
from yaml import Dumper, Loader

# Configure logger lg with config for appLogger from config.json["logging"]
with open("setup_project/config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")


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

    def add_commands(self, command_list, losc=False):
        """
        Add a list of commands to self.commands.

        Args:
            command_list:
            (str): A string of commands seperated by spaces
            (list): A list of string commands
            losc (bool): Whether we are passing a list of string commands that
                        need to be split individually

        Returns:
            None
        """

        if not command_list:
            raise AttributeError(
                "Empty list or string passed to add_commands method"
            )

        if type(command_list) == str:
            command = command_list.split(" ")
            self.commands.append(command)
        elif losc == True:
            for base_string in command_list:
                command = base_string.split(" ")
                self.commands.append(command)
        else:
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
        if not command:
            raise AttributeError("Empty command list")
        if type(command) != list:
            raise TypeError("Command should be a list")
        # run the command
        result = run(command, stdout=subprocess.PIPE, shell=True)
        # decode output from bytes to UTF-8 encoded string
        stdout = result.stdout.decode("utf-8")
        # return output
        return stdout

    def file_extract(self, file_name):
        """
        Extracts yaml strings from a file

        Args:
            file_name (string): Name of the file

        Returns:
            command_list (dict): yaml extracted from file
        """
        # Check if file name has been passed
        if not file_name:
            raise ValueError("Empty filename")
        # Check if file exists
        if not os.path.exists(f"./{file_name}"):
            raise FileNotFoundError(f"{file_name} doesn't exist")
        # check if file is a zip file
        if file_name[-4:] != ".yml":
            if file_name[-5:] != ".yaml":
                raise ValueError(
                    f"{file_name}: File extension should be yml or yaml"
                )

        with open(file_name, "r") as stream:
            yaml_object = yaml.load(stream, Loader=Loader)

        return yaml_object

    def log_output(self, command, output):
        """
        Writes output to log

        Args:
            command (string): String of command to be logged.
            output (string): String of output to be logged.

        Returns:
            None
        """
        if not command:
            raise ValueError("Empty command or output")
        if not output:  # pragma: no cover
            output = "Empty output"
        lg.info("Command:")
        lg.info(command)
        lg.info("Output:")
        lg.info(output)

    def run_commands(self):
        """
        Runs all the commands in the commands attribute of the object, and
        deletes them. Writes output to setup.log.

        Args:
            None

        Returns:
            None
        """
        if not self.commands:
            raise ValueError("Empty Command List")
        # run all the commands
        for command in self.commands:
            output = self.execute_cmd(command)
            self.log_output(command, output)

        # Clear the list of commands
        self.delete_commands()

    def substitute_values(self, command_data):
        """
        Substitutes attributes in commands at locations.

        Args:
            command_data (yaml): A yaml object that contains:
                commands (string): string commands sub and loc
                substitutions (dict): dictionary that contains
                sub (list): list of string attributes
                loc (list): list of string locations

        Returns:
            cmd_list (list): A list of string commands
        """
        if not command_data:
            raise (
                TypeError(
                    "Pass only yaml objects to substitute.Or Empty yaml object passed."
                )
            )
        elif type(command_data) != dict:
            raise (TypeError("Pass only yaml objects to substitute"))

        if not command_data["commands"]:
            raise (ValueError("Empty command list"))

        substitutions = command_data["substitutions"]
        cmd_list = []
        commands = command_data["commands"]
        content = commands
        for substitution in substitutions:
            sub_word = substitution["sub"]
            loc_len = len(substitution["loc"])
            for i in range(loc_len):
                content = content.replace(substitution["loc"][i], sub_word)

        cmd_list = content.split("\n")[:-1]
        return cmd_list

    def operate(self, file_name):  # pragma: no cover
        """
        Operates the setup

        Args:
            file_name (string): Name of the file

        Returns:
            bool :
                True if it works
                False if it doesn't
        """
        try:
            self.delete_commands()
            command_data = self.file_extract(file_name)
            commands = self.substitute_values(command_data=command_data)
            self.add_commands(commands, losc=True)
            self.run_commands()
            return True
        except Exception as e:
            lg.error(e)
            return False
