#!/usr/bin/env python
from distutils.core import setup


setup(
    name='blanc-basic-assets',
    version='0.1',
    description='Blanc Basic Assets for Django',
    long_description=open('README.rst').read(),
    url='http://www.blanctools.com/',
    maintainer='Alex Tomkins',
    maintainer_email='alex@hawkz.com',
    platforms=['any'],
    packages=[
        'blanc_basic_assets',
        'blanc_basic_assets.assets',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='BSD-2',
)
