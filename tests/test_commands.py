"""
Tests for setup_project.Commands
"""

import os

import pytest
import yaml

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
        x = Commands()
        test_cmd_string = "git status"
        test_cmd_string_result = [
            "git",
            "status",
        ]
        test_cmd_list = [
            "test_project_setup-env\\Scripts\\python.exe",
            "-m",
            "pip",
            "list",
        ]

        x.add_commands(test_cmd_string)
        assert test_cmd_string_result in x.commands, "String not in list"

        x.add_commands(test_cmd_list)
        assert [
            "test_project_setup-env\\Scripts\\python.exe",
            "-m",
            "pip",
            "list",
        ] in x.commands, "List not in list"

        x.add_commands(["echo hello", "echo Working as intended"], losc=True)
        assert ["echo", "hello"] in x.commands, "List not in list"

        assert [
            "echo",
            "Working",
            "as",
            "intended",
        ] in x.commands, "List not in list"

    def test_add_commands_exception(self):
        x = Commands()
        test_cmd_string = ""

        with pytest.raises(AttributeError) as e:
            x.add_commands(test_cmd_string)

        assert "Empty list or string passed to add_commands method" in str(
            e.value
        )

        with pytest.raises(AttributeError) as e:
            x.add_commands([])

        assert "Empty list or string passed to add_commands method" in str(
            e.value
        )

    def test_delete_commands(self):
        x = Commands()
        test_cmd_string = "C:\\Program Files\\Git\\bin\\git.exe status"
        x.add_commands(test_cmd_string)
        x.delete_commands()

        assert not x.commands, "Command list not empty"

    def test_execute_cmd(self):
        x = Commands()

        command1 = ["echo", "Hello"]

        command2 = [
            "setup_project-env\\Scripts\\python.exe",
            "-m",
            "pip",
            "--version",
        ]

        result = x.execute_cmd(command1)

        assert result == "Hello\r\n", "Invalid command output1"

        os.chdir("../")

        result = x.execute_cmd(command2)

        content = "pip 20.2 from J:\\Education\\Code\\Python\\Project-Setup\\setup_project-env\\lib\\site-packages\\pip (python 3.8)\r\r\n"

        os.chdir("tests/")

        assert content == result, "Invalid command output2"

    def test_execute_cmd_exception(self):
        x = Commands()

        with pytest.raises(AttributeError) as e:
            x.execute_cmd([])

        assert "Empty command list" in str(e.value)

        with pytest.raises(TypeError) as e:
            x.execute_cmd("Test string")

        assert "Command should be a list" in str(e.value)

    def test_file_extract(self):
        x = Commands()
        result = x.file_extract("test_yaml.yml")

        test_dict = {
            "commands": ["Hello", "Cats", "Are So", "Small"],
            "substitutions": [{"sub": "Dogs"}, {"loc": ["Cats", "Small"]}],
        }

        assert result == test_dict, "File load mismatch"

        x = Commands()
        result = x.file_extract("test_cmd.yml")

        test_dict = {
            "commands": [
                "echo hello",
                "echo Working as intended",
                "john Substitutions are also working",
                "henry Substitutions are also working in multiple locations",
            ],
            "substitutions": [{"sub": "echo"}, {"loc": ["john", "henry"]}],
        }

        assert result == test_dict, "File load mismatch"

    def test_file_extract_exception(self):
        x = Commands()

        with pytest.raises(FileNotFoundError) as e:
            x.file_extract("Cats.yml")

        assert "Cats.yml doesn't exist" in str(e.value)

        with pytest.raises(ValueError) as e:
            x.file_extract("")

        assert "Empty filename" in str(e.value)

        with pytest.raises(ValueError) as e:
            x.file_extract("app.log")

        assert "File extension should be yml or yaml" in str(e.value)

    def test_log_output(self):
        x = Commands()
        output = """- sub\n- loc\n- Cats\n- Small"""
        commands = """- Hello\n- Cats\n- Are So\n- Small"""
        x.log_output(commands, output)

        test_content = "Command:\n- Hello\n- Cats\n- Are So\n- Small\nOutput:\n- sub\n- loc\n- Cats\n- Small\n"

        os.chdir("../")

        with open("setup.log") as f:
            content = f.read()

        os.chdir("tests/")

        assert content == test_content, "File data mismatch"

    def test_log_output_exception(self):
        x = Commands()

        with pytest.raises(ValueError) as e:
            x.log_output("", "a")

        assert "Empty command or output" in str(e.value)

        with pytest.raises(ValueError) as e:
            x.log_output("a", "")

        assert "Empty command or output" in str(e.value)

    def test_run_commands(self):
        x = Commands()

        x.add_commands(["echo hello", "echo Working as intended"], losc=True)
        x.run_commands()

        test_content = "Command:\n- Hello\n- Cats\n- Are So\n- Small\nOutput:\n- sub\n- loc\n- Cats\n- Small\nCommand:\n['echo', 'hello']\nOutput:\nhello\n\n\nCommand:\n['echo', 'Working', 'as', 'intended']\nOutput:\nWorking as intended\n\n\n"
        os.chdir("../")

        with open("setup.log") as f:
            content = f.read()

        os.chdir("tests/")

        assert content == test_content, "Run commands output mismatch"

    def test_substitute_values(self):
        x = Commands()
        yaml_object = yaml.load(
            """
        commands:
        - echo hello
        - echo Working as intended
        - john Substitutions are also working
        - henry Substitutions are also working in multiple locations
        substitutions:
        - sub: echo
        - loc:
            - john
            - henry
        """
        )

        result = x.substitute_values(yaml_object)

        test_content = [
            "echo hello",
            "echo Working as intended",
            "echo Substitutions are also working",
            "echo Substitutions are also working in multiple locations",
        ]

        assert result == test_content, "Substituted words don't match"

    def test_substitute_values_exception(self):
        x = Commands()

        yaml_object = yaml.load(
            """
        ---

        """
        )

        with pytest.raises(ValueError) as e:
            x.substitute_values(yaml_object)

        assert "Empty yaml object" in str(e.value)

        with pytest.raises(TypeError) as e:
            x.substitute_values("")

        assert "Pass only yaml objects to substitute" in str(e.value)

    def test_substitute_value(self):
        x = Commands()

        command = "john Substitutions are also working"
        attribute = "echo"
        location = "john"

        result = x.substitute_value(command, attribute, location)

        assert result == "echo Substitutions are also working"

        command = "henry Substitutions are also working in multiple locations"
        attribute = "echo"
        location = "henry"

        result = x.substitute_value(command, attribute, location)

        assert (
            result
            == "echo Substitutions are also working in multiple locations"
        )

    def test_substitute_value_exception(self):
        x = Commands()

        with pytest.raises(ValueError) as e:
            x.substitute_value("", "a", "a")

        assert "Empty command or output" in str(e.value)

        with pytest.raises(ValueError) as e:
            x.substitute_value("a", "", "a")

        assert "Empty command or output" in str(e.value)

        with pytest.raises(ValueError) as e:
            x.substitute_value("a", "a", "")

        assert "Empty command or output" in str(e.value)

        with pytest.raises(TypeError) as e:
            x.substitute_value("1", "1", 1)

        assert "Pass only strings to substitute" in str(e.value)

        with pytest.raises(TypeError) as e:
            x.substitute_value(1, "a", "a")

        assert "Pass only strings to substitute" in str(e.value)

        with pytest.raises(TypeError) as e:
            x.substitute_value("1", 1, "1")

        assert "Pass only strings to substitute" in str(e.value)

    def test_operate(self):
        x = Commands()
        x.operate("test_cmd.yml")
        test_content = """
        hello

        Working as intended

        Substitutions are also working

        Substitutions are also working in multiple locations


        """

        with open("setup.log") as f:
            content = f.read()

        assert content == test_content, "Operate output mismatch"
