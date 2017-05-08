#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Monte Carlo Simulator for Pandas
# https://github.com/ranaroussi/pandas-montecarlo

"""Monte Carlo Simulator for Pandas"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pandas-montecarlo',
    version="0.0.2",
    description='Monte Carlo Simulator for Pandas',
    long_description=long_description,
    url='https://github.com/ranaroussi/pandas-montecarlo',
    author='Ran Aroussi',
    author_email='ran@aroussi.com',
    license='LGPL',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 3 - Alpha',

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    platforms = ['any'],
    keywords='montecarlo simulator, monte carlo, monte carlo simulation, montecarlo simulation',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['pandas', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)