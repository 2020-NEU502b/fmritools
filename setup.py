#! /usr/bin/env python
#
# Copyright (c) 2019 Princeton Neuroscience Institute
# https://github.com/2019-NEU502b

import os, sys
from setuptools import setup, find_packages
path = os.path.abspath(os.path.dirname(__file__))

## Metadata
DISTNAME = 'fmritools'
MAINTAINER = 'PNI'
MAINTAINER_EMAIL = 'PrincetonNeuro@princeton.edu'
DESCRIPTION = 'Useful tools for fMRI experiment design and analysis'
URL = 'http://pni.princeton.edu'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/2019-NEU502b'

with open(os.path.join(path, 'README.md'), encoding='utf-8') as readme_file:
    README = readme_file.read()

with open(os.path.join(path, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

VERSION = None
with open(os.path.join('fmritools', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            VERSION = line.split('=')[1].strip().strip('\'')
            break
if VERSION is None:
    raise RuntimeError('Could not determine version')

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=README,
      packages=find_packages(exclude=['docs', 'tests']),
      install_requires=requirements,
      license=LICENSE
)
