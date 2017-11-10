#!/usr/bin/env python
from codecs import open

from setuptools import find_packages, setup

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='blanc-basic-assets',
    version='0.3.3',
    description='Blanc Basic Assets for Django',
    long_description=readme,
    url='https://github.com/developersociety/blanc-basic-assets',
    maintainer='Developer Society',
    maintainer_email='studio@dev.ngo',
    platforms=['any'],
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='BSD',
)
