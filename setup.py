
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Jagriti',
    author_email='jagriti2425@gmail.com',
    install_requires=[
        'pandas==2.0.3',
        'numpy==1.24.4',
        'seaborn==0.13.2',
        'flask==3.0.3'
    ],
    packages=find_packages()
)