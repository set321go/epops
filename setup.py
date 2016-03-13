# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='epops',
    version='0.0.1',
    description='Elastic path Operations Framework',
    long_description=readme,
    author='Elastic Path',
    author_email='pd@elasticpath.com',
    url='https://github.com/aedwards/epops',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='nose.collector',
    tests_require=[
        'nose',
    ],
    install_requires=[
        'requests>=2.9.1',
        'paramiko>=1.16.0',
        'pyyaml>=3.11',
        'watchdog>=0.8.3',
        'yapsy>=1.11.223'
    ],
    entry_points={
        'console_scripts': ['epops=core.main:main']
    }
)

