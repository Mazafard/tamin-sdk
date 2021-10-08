#!/usr/bin/env python

import sys

import setuptools

dependencies = [
    'requests >= 2.0.0',
    'guzzle_sphinx_theme',
]

if sys.version_info < (3, 4):
    dependencies.append('enum34')

with open('PYPI_DESCRIPTION.rst') as file:
    long_description = file.read()

setuptools.setup(
    name='taminsdk',
    author='Mazafard',
    url='https://github.com/mazafard/tamin-sdk',
    author_email='mazafard@gmail.com',
    version='0.3.0',
    description='Unoffical Tamin SDK',
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=setuptools.find_packages(),
    install_requires=dependencies,
)
