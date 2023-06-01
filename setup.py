#!/usr/bin/env python
"""
An interface to the Pluggable Authentication Modules (PAM) library,
written in pure Python (using ctypes).
"""

import sys

from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg


class bdist_egg_disabled(bdist_egg):
    """Disabled version of bdist_egg

    Prevents setup.py install from performing setuptools' default easy_install,
    which it should never ever do.
    """

    def run(self):
        sys.exit(
            "Aborting implicit building of eggs. Use `pip install .` to install from source."
        )


with open('pamela.py') as f:
    for line in f:
        if line.startswith('__version__'):
            version_ns = {}
            exec(line, version_ns)
            version = version_ns['__version__']


setup(
    name='pamela',
    version=version,
    description="PAM interface using ctypes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
    ],
    cmdclass={
        "bdist_egg": bdist_egg if "bdist_egg" in sys.argv else bdist_egg_disabled,
    },
    keywords=['pam', 'authentication'],
    author='Min RK',
    author_email='benjaminrk@gmail.com',
    url='https://github.com/minrk/pamela',
    license='MIT',
    py_modules=["pamela"],
)
