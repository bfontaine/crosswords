# -*- coding: UTF-8 -*-

from os.path import dirname
import sys

import setuptools
from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='crosswords/__init__.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

setup(
    name='crosswords',
    version=verstr,
    author='Baptiste Fontaine',
    author_email='b@ptistefontaine.fr',
    packages=['crosswords'],
    url='https://github.com/bfontaine/crosswords',
    license=open('LICENSE', 'r').read(),
    description='2048 in your terminal',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'Unidecode==0.04.14',
    ],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts':[
            'crosswords = crosswords.cli:run'
        ]
    },
)
