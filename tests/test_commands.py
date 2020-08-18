"""
Tests for setup_project.Commands
"""

import os

import pytest

import setup_project
from setup_project import Commands, commands


def test_helloworld(capsys):
    """ Correct object argument prints """
    commands.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


def test_helloworld_exception():
    with pytest.raises(TypeError):
        commands.helloworld(1)


class TestCommands(object):
    def test__init__(self):
        x = Commands()
        if not x.commands:
            x.commands.append("command")
            assert "command" in x.commands

    def test_add_commands(self):
        pass

    def test_add_commands_exception(self):
        pass

    def test_delete_commands(self):
        pass

    def test_execute_cmd(self):
        pass

    def test_file_extract(self):
        pass

    def test_log_output(self):
        pass

    def test_run_commands(self):
        pass

    def test_substitute_values(self):
        pass

    def test_substitute_value(self):
        pass

    def test_operate(self):
        pass
