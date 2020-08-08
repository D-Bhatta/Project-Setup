from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="setup_project",
    version="v0.0.1-alpha.4",
    author="D-Bhatta",
    author_email="dbhatta1232@gmail.com",
    description="A set of scripts to quickly setup a project",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/D-Bhatta/Project-Setup.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
