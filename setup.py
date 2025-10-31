import re
from os.path import join, dirname

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'fireball', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 2.6.13',
    'redis == 2.10.6'
]


setup(
    name='fireball',
    author='Mohammad Faezi',
    author_email='faezi.h.m@gmail.com',
    version=package_version,
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='fireball.tests',
    entry_points={
        'console_scripts': [
            'fireball = fireball:fireball.cli_main'
        ]
    }
)

