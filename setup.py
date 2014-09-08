#!/usr/bin/env python

from setuptools import setup
from kubpy import __version__


setup(
    name = 'kubpy',
    version=__version__,
    description = 'Python client for Kubernetes REST API',
    author = 'Andriy Yurchuk',
    author_email = 'ayurchuk@minuteware.net',
    url = 'https://github.com/Ch00k/kubpy',
    license = 'LICENSE.txt',
    long_description = open('README.rst').read(),
    entry_points = {
      'console_scripts': [
          'kubpy = kubpy.kubpy:main'
      ]
    },
    packages = ['kubpy'],
)