#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


reqs = parse_requirements('requirements.txt')

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# version
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here, 'comnamepy', '__init__.py'))
                if line.startswith('__version__ = ')), '0.0.dev0')

setup(
    name="comnamepy",
    version=version,
    url='https://github.com/heku777/comnamepy',
    author='heku777',
    author_email='chotips08@gmail.com',
    maintainer='heku777',
    maintainer_email='chotips08@gmail.com',
    description='Get the company name from the domain.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=reqs,
    zip_safe=False,
    python_requires='>=3.6',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'comname=comnamepy.comnamepy:main',
        ],
    },
)
