#!/usr/bin/env python

from setuptools import setup

setup(
    name="OnionPy",
    version="0.1.2",
    description="Python wrapper for the OnionOO tor status API",
    long_description=open('README.txt').read(),
    author="Lukas Erlacher",
    author_email="tor@lerlacher.de",
    url="http://github.com/duk3luk3/onion-py",
    packages=['onion_py'],
    scripts=['bin/onion.py'],

    extras_require = {
      'Query caching': ['pymemcache>=1.2.1']
      },
    dependency_links = [
      'git+https://github.com/pinterest/pymemcache.git'
      ],
    )
