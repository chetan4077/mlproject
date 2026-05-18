# automatically finds out all packages in project dir
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    #this fn will return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='mlProject',
    version=0.1,
    author='Chetan',
    email='skylord21303@gmail.com',
    packages=find_packages(), # the places wherever __init__.py is present that will be considered as a package
    install_requires=get_requirements('requirement.txt')
)
