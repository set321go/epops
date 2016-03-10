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
    install_requires=[
        'requests',
        'paramiko',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': ['epops=core.main:main']
    }
)

