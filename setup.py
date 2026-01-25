from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Myapp",
    version="0.1",
    author="Santosh Bambrule",
    packages=find_packages(),
    install_requires = requirements,
)