# coding: utf-8

from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name="sapcai",
    version="4.0.0",
    packages=find_packages(),
    description="SAP Conversational AI official SDK for python",
    long_description=readme,
    author="SAP CAI team",
    url="https://github.com/SAPConversationalAI/sdk-python",
    license="MIT",
    install_requires=[
      "requests>=2.10",
      "pytest>=2.9",
      "pytest-cov>=2.2",
      "responses>=0.5"
    ],
    keywords="sapcai bot nlp")
