""" Tests for 'setup_project' package """
import pytest

from setup_project import setup_project


def test_helloworld(capsys):
    """ Correct object argument prints """
    setup_project.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


def test_helloworld_exception():
    with pytest.raises(TypeError):
        setup_project.helloworld(1)
