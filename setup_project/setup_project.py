""" Sets up a python project in a directory """
import os
import shutil


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


def zip_push(sourcedir="project-name", zip_name="project_name"):
    """
    Zips up the files in the source directory

    Args:
        sourcedir (str): Path of the source directory.
        zip_name (str): Name of the output zip file.

    Returns:
        None
    """
    # Create zip file
    shutil.make_archive(zip_name, "zip", sourcedir)


def zip_pop(file_name="project_name.zip"):
    """
    Unzips a zip file into the current directory

    Args:
        file_name (str): Name of the zip file. Must have a supported extension.
                         one of “zip”, “tar”, “gztar”, “bztar”, or “xztar”. Or
                         any other format registered with
                         register_unpack_format().

    Returns:
        None
    """
    shutil.unpack_archive(filename=file_name)


def del_file(file_name="project_name.zip"):
    """
    Utility function to delete a file.

    Args:
        file_name (str): Name of the file.

    Returns:
        None
    """
    os.remove(file_name)


if __name__ == "__main__":
    zip_pop()
