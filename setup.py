# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import filtered_feed

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = filtered_feed.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django_filtered_feed',
    version=version,
    description='Feeds sans noise.',
    long_description=readme + '\n\n' + history,
    author='Ali Zaidi',
    author_email='alixedi@gmail.com',
    url='https://github.com/alixedi/django_filtered_feed',
    packages=[
        'filtered_feed',
    ],
    include_package_data=True,
    install_requires=[
        'django-filter==0.7',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django_filtered_feed',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)