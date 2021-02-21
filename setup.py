"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='TriplesLab',
      version='0.1.0',
      author='Ed Sweeney',
      description='An exploration of rdflib.',
      long_description=long_description,
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'TriplesLab = TriplesLab.__main__:main'
          ]
      })
