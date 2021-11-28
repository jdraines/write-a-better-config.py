from setuptools import setup, find_packages

setup(
    name="hello_world",
    version="1.0",
    description="An application for demonstrating config.py techniques",
    install_requires=[
        "termcolor==1.1.0",
        "pyyaml==6.0"
    ],
    packages=find_packages()
)