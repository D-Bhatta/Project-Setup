"""
Tests for setup_project.Commands
"""

import os

import pytest

import setup_project
from setup_project import Commands

os.chdir("tests/")


def test_helloworld(capsys):
    """ Correct object argument prints """
    Commands.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


def test_helloworld_exception():
    with pytest.raises(TypeError):
        Commands.helloworld(1)


class TestCommands(object):
    def test__init__(self):
        pass

    def test_add_commands(self, command_list):
        pass

    def test_add_commands_exception(self, command_list):
        pass

    def test_delete_commands(self):
        pass

    def test_execute_cmd(self, command):
        pass

    def test_file_extract(self, file_name):
        pass

    def test_log_output(self, output):
        pass

    def test_run_commands(self):
        pass

    def test_substitute_values(self, command_data):
        pass

    def test_substitute_value(self, command, attribute):
        pass

    def test_operate(self):
        pass
