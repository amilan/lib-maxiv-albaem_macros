#!/usr/bin/env python

###############################################################################
#     lib-maxiv-albaem_macros
#
#     Copyright (C) 2017  MAX IV Laboratory, Lund Sweden.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

from setuptools import setup, find_packages


def main():
    """Main method collecting all the parameters to setup."""
    name = "lib-maxiv-albaem_macros"

    version = "0.1.0"

    description = "Sardana macros for the new alba electrometer (EM#)"

    author = "antmil"

    author_email = "antonio.milan_otero@maxiv.lu.se"

    license = "GPLv3"

    url = "http://www.maxiv.lu.se"

    packages = find_packages()

    provides = ["albaem_macros"]

    # requires = ['sardana']

    setup(
        name=name,
        version=version,
        description=description,
        author=author,
        author_email=author_email,
        license=license,
        url=url,
        packages=packages,
    )

if __name__ == "__main__":
    main()
