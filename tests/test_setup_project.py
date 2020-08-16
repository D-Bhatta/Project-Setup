""" Tests for 'setup_project' package """
import os

import pytest

from setup_project import setup_project

os.chdir("tests/")


def test_helloworld(capsys):
    """ Correct object argument prints """
    setup_project.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


def test_helloworld_exception():
    with pytest.raises(TypeError):
        setup_project.helloworld(1)


def test_zip_push():
    name = setup_project.zip_push("./project_name", "project_name")
    assert name == "project_name.zip", "File name mismatch"


def test_zip_push_exception():
    with pytest.raises(ValueError) as e:
        setup_project.zip_push("")

    assert "Directory doesn't exist" in str(e.value)


def test_zip_push_exception2(capsys):
    setup_project.zip_push(sourcedir="hello")
    captured = capsys.readouterr()
    assert "Source directory doesn't exist" in captured.out


def test_zip_push_exception3():
    with pytest.raises(ValueError) as e:
        setup_project.zip_push(file_name="")

    assert "Empty filename" in str(e.value)


def test_zip_pop():
    assert (
        setup_project.zip_pop("./project_name.zip") == True
    ), "Unzip operation failure"
    if os.path.exists("test_fixture.txt"):
        os.remove("test_fixture.txt")


def test_zip_pop_exception():
    with pytest.raises(ValueError) as e:
        setup_project.zip_pop("")

    assert "Empty filename" in str(e.value)


def test_zip_pop_exception2():
    with pytest.raises(ValueError) as e:
        setup_project.zip_pop("cat.mzip")

    assert "File extension should be zip" in str(e.value)


def test_zip_pop_exception3():
    with pytest.raises(FileNotFoundError) as e:
        setup_project.zip_pop("cat.zip")

    assert "cat.zip doesn't exist" in str(e.value)


def test_del_file():
    assert (
        setup_project.del_file("./project_name.zip") == True
    ), "Delete operation failure"


def test_del_file_exception():
    with pytest.raises(ValueError) as e:
        setup_project.del_file("")

    assert "Empty filename" in str(e.value)


def test_del_file_exception2():
    with pytest.raises(FileNotFoundError) as e:
        setup_project.del_file("cat.zip")

    assert "cat.zip doesn't exist" in str(e.value)
