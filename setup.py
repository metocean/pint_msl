#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(name='pint_msl',
          version='1.3',
          description='Pint unit registry with extra definitions',
          author='MetOcean Solutions',
          author_email='ops@metocean.co.nz',
          url='https://github.com/metocean/pint_msl',
          install_requires=['pint >= 0.8'],
          # package_dir={''},
          packages=find_packages(),
          classifiers=[
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
            'Programming Language :: Python :: 3.14',
          ],
    )
