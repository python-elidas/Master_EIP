'''Insatalador para el paquete 'primos' '''

from setuptools import setup

long_description = (
    open('Readme.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n'
)

setup(
    name = 'elidas_primos',
    version = '1.0',
    description='A tool to get primal numbers in a range',
    long_description = long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    keywords = 'pyoperaciones mathematical operations',
    author = 'Oscar Gutierrez',
    license = 'GNUGPLv3',
    packages = ['elidas_primos']
)
