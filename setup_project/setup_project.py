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


def zip_push(sourcedir="project_name", file_name="project_name"):
    """
    Zips up the files in the source directory

    Args:
        sourcedir (str): Path of the source directory.
        zip_name (str): Name of the output zip file.

    Returns:
        name (str): Name of the output zip file.
    """
    if not file_name:
        raise ValueError("Empty filename")
    if not sourcedir:
        raise ValueError("Directory doesn't exist")
    # Create zip file
    # Get full path of zip file created
    name = ""
    try:
        name = shutil.make_archive(file_name, "zip", sourcedir)
    except FileNotFoundError:
        print("Source directory doesn't exist")

    # get the start of the file name
    start = 0 - (len(file_name + "zip") + 1)

    # extract the filename from the full path
    name = name[start:]

    return name


def zip_pop(file_name="project_name.zip", ext_dir=None):
    """
    Unzips a zip file into the current directory

    Args:
        file_name (str): Name of the zip file. Must have a supported extension.
                         one of “zip”, “tar”, “gztar”, “bztar”, or “xztar”. Or
                         any other format registered with
                         register_unpack_format().

    Returns:
        bool: True if operation succeeded, False if not
    """
    # Check if file name has been passed
    if not file_name:
        raise ValueError("Empty filename")

    # check if file is a zip file
    if file_name[-4:] != ".zip":
        raise ValueError("File extension should be zip")

    # Check if file exists
    if not os.path.exists(f"./{file_name}"):
        raise FileNotFoundError(f"{file_name} doesn't exist")
    else:
        # unzip archive
        shutil.unpack_archive(filename=file_name, extract_dir=ext_dir)
        # return status
        return True


def del_file(file_name="project_name.zip"):
    """
    Utility function to delete a file.

    Args:
        file_name (str): Name of the file.

    Returns:
        None
    """
    # Check if file name has been passed
    if not file_name:
        raise ValueError("Empty filename")

    # Check if file exists
    if not os.path.exists(f"./{file_name}"):
        raise FileNotFoundError(f"{file_name} doesn't exist")
    else:
        os.remove(file_name)
        return True


if __name__ == "__main__":  # pragma: no cover
    zip_push()
