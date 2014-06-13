#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='blanc-basic-assets',
    version='0.3',
    description='Blanc Basic Assets for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/blancltd/blanc-basic-assets',
    maintainer='Alex Tomkins',
    maintainer_email='alex@blanc.ltd.uk',
    platforms=['any'],
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    license='BSD',
)
