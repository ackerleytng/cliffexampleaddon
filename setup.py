#!/usr/bin/env python

PROJECT = 'cliffexampleaddon'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.me', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Addon to demo app for cliff',
    long_description=long_description,

    author='Ackerley Tng',
    author_email='ackerleytng@gmail.com',

    url='https://github.com/ackerleytng/cliffexampleaddon',
    download_url='https://github.com/ackerleytng/cliffexampleaddon/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliffdemo'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'cliff.demo': [
            'addon = cliffexampleaddon.addon:Addon',
        ],
    },

    zip_safe=False,
)
