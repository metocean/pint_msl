#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

install_requires = [
    'pint >= 0.8',
    ]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(name='pint_msl',
          version='0.1',
          description='Pint unit registery with extra definitions',
          author='MetOcean Solutions',
          author_email='ops@metocean.co.nz',
          url='https://github.com/metocean/pint_msl',
          install_requires=install_requires,
          )
