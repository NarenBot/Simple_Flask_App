from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Naren"
DESCRIPTION = "This is a housing prediction project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: Returns all libraries present inside requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as req_file:
        req_file.readlines().remove("-e .")


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()

)

