from setuptools import setup
from recastai.utils import Utils

setup(
    name="recastai",
    version=Utils.VERSION,
    py_modules=["recastai"],
    description="Recast.AI official SDK for python",
    author="Paul Renvoise",
    author_email="paul.renvoise@recast.ai",
    url="https://github.com/RecastAI/sdk-python",
    long_description=open('README.md').read())
