#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(name='pint_msl',
          version='0.2',
          description='Pint unit registery with extra definitions',
          author='MetOcean Solutions',
          author_email='ops@metocean.co.nz',
          url='https://github.com/metocean/pint_msl',
          install_requires=['pint >= 0.8'],
          )
