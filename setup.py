from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SimpleLoginAndRegister',
    version='1.0.0',
    description='A Basic Login and Registration System',
    long_description=long_description,
    url='https://github.com/coolhobo77/Python-Login-And-Register',
    author='coolhobo77',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Authentication',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='simple login register authenticate auth authentication',
    packages=find_packages(py_modules=["Login.py"]),
)
