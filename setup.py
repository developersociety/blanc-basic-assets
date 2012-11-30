#!/usr/bin/env python
from distutils.core import setup

# Use blanc_basic_assets.VERSION for version numbers
version_tuple = __import__('blanc_basic_assets').VERSION
version = '.'.join([str(v) for v in version_tuple])

setup(
    name='blanc-basic-assets',
    version=version,
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
    package_data={'blanc_basic_assets': [
        'assets/templates/admin/assets/*.html',
        'assets/templates/admin/assets/file/*.html',
        'assets/templates/admin/assets/image/*.html',
    ]},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='BSD-2',
)
