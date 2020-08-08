""" Tests for 'project-name' package """
import pytest
from project_name import project_name


def test_helloworld(capsys):
    """ Correct object argument prints """
    project - name.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


# This is supposed to fail
def test_helloworld_exception():
    with pytest.raises(TypeError):
        project - name.helloworld("1")