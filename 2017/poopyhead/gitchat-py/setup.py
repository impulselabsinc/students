# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gitchat',
    version='0.1.0',
    description='Applet to teach children how to use Github',
    long_description=readme,
    author='Nikhil Prabhakar',
    author_email='nikhil@impulselabs.io',
    url='https://github.com/impulselabsinc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

