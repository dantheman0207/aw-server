#!/usr/bin/env python

from setuptools import setup

setup(name='aw-server',
      version='0.1',
      description='ActivityWatch server',
      author='Erik Bjäreholt',
      author_email='erik@bjareho.lt',
      url='https://github.com/ActivityWatch/aw-server',

      packages=['aw_server'],

      include_package_data=True,

      install_requires=[
          'aw-core>=0.1.0',
          'flask>=0.10',
          'flask-restplus>=0.9.2',
          'flask-cors>=2.1',
          'pymongo>=3.2',
          'appdirs>=1.4.0',
          'python-json-logger>=0.1.5'
      ],
      dependency_links=[
          'https://github.com/ActivityWatch/aw-core/tarball/master#egg=aw-core-0.1'
      ],

      entry_points={
          'console_scripts': ['aw-server = aw_server:main']
      })
