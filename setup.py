#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='cieloApi3',
    version='0.1.9',
    description='SDK API-3.0 Python Cielo',
    author='Thiago Malaquias / Fernando Canteruccio',
    author_email='thiago.malaca@gmail.com / fernando.canteruccio@gmail.com',
    url='https://github.com/naripok/API-3.0-Python',
    keywords='api3.0 cielo python sdk ecommerce',
    packages=find_packages(),
    install_requires=['requests', 'future'],
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    )
)


setup(**settings)
