from setuptools import find_packages, setup
from typing import List

hypen_e_dot = "-e ."  #-e. will trigger the setup.py while downloading packages

def get_requirements(file_path:str)->List[str]:
    """
    THIS FUNCTION WILLRETURN THE LIST OF REQUIREMENTS
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        """This readlines will add \n at end"""
        requirements = [req. replace("\n","") for req in requirements]

        if hypen_e_dot in requirements: 
            requirements.remove(hypen_e_dot)
    return requirements


setup(
name="students-performance",
version="0.0.1",
author="Rounak",
author_email="raunakgupta914@gmail.com",
packages= find_packages(),
install_requires = get_requirements("requirements.txt")

)