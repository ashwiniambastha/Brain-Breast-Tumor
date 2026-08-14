# to make our modular logic into package
# once the project is complete , 
## try to upload this package to pypi

from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="brain-breast-cancer",
    version="0.2",
    author="dmt",
    packages=find_packages(),
    install_requires = requirements,
)