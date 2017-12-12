#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2016 wolfSSL Inc.
#
# This file is part of wolfSSL. (formerly known as CyaSSL)
#
# wolfSSL is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# wolfSSL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

# pylint: disable=wrong-import-position

import sys
import pip
from setuptools import setup
from setuptools.command.build_ext import build_ext

sys.path.insert(0, "src")

import wolfcrypt
from wolfcrypt._build_wolfssl import build_wolfssl

# long_description
with open("README.rst") as readme_file:
    long_description = readme_file.read()

with open("LICENSING.rst") as licensing_file:
    long_description = long_description.replace(".. include:: LICENSING.rst\n",
                                                licensing_file.read())

# requirements
def _parse_requirements(filepath):
    raw = pip.req.parse_requirements(
        filepath, session=pip.download.PipSession())

    return [str(i.req) for i in raw]

install_requirements = _parse_requirements("requirements/prod.txt")
setup_requirements = _parse_requirements("requirements/setup.txt")
test_requirements = _parse_requirements("requirements/test.txt")

class cffiBuilder(build_ext, object):

    def build_extension(self, ext):
        """ Compile manually the wolfcrypt-py extension, bypass setuptools
        """
        build_wolfssl(wolfcrypt.__wolfssl_version__)

        super(cffiBuilder, self).build_extension(ext)

setup(
    name="wolfcrypt",
    version=wolfcrypt.__version__,
    description= \
        u"Python module that encapsulates wolfSSL's crypto engine API.",
    long_description=long_description,
    author=wolfcrypt.__author__,
    author_email=wolfcrypt.__email__,
    url="https://github.com/wolfssl/wolfcrypt-py",
    packages=["wolfcrypt"],
    package_dir={"":"src"},
    cffi_modules=["./src/wolfcrypt/_build_ffi.py:ffi"],
    license="GPLv2 or Commercial License",
    zip_safe=False,
    keywords="wolfssl, wolfcrypt, security, cryptography",
    classifiers=[
        u"License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        u"License :: Other/Proprietary License",
        u"Operating System :: OS Independent",
        u"Programming Language :: Python :: 2.7",
        u"Programming Language :: Python :: 3.4",
        u"Programming Language :: Python :: 3.5",
        u"Programming Language :: Python :: 3.6",
        u"Topic :: Security",
        u"Topic :: Security :: Cryptography",
        u"Topic :: Software Development"
    ],
    setup_requires=setup_requirements,
    install_requires=install_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    cmdclass={"build_ext" : cffiBuilder}
)
