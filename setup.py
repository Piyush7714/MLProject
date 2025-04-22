from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirnments(file_path:str)->List[str]:
    requirnments=[]
    with open(file_path) as file_obj:
        requirnments=file_obj.readlines()
        requirnments=[req.replace("\n"," ")for req in requirnments]
        if HYPEN_E_DOT in requirnments:
            requirnments.remove(HYPEN_E_DOT)

    return requirnments






setup(
    name="ML Project",
    version='0.0.1',
    author='Piyush',
    password=find_packages(),
    install_requires=get_requirnments('requirnments.txt')


)