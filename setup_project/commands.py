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
        if not output:
            raise ValueError("Empty command or output")
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
