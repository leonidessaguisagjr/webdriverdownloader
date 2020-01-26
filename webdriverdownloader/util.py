"""
Module for utility functions.

This code is released under the MIT license.
"""
import sys


def get_architecture_bitness() -> str:
    """
    Function for getting the "bitness" of the underlying architecture i.e. if it is 32-bit or 64-bit.  Code is based
    on the following:

     https://docs.python.org/3/library/platform.html#cross-platform

    :return: The bitness of the underlying architecture, as a str i.e. "32" or "64"
    """
    # TODO: Try using py-cpuinfo https://pypi.org/project/py-cpuinfo/
    return "64" if sys.maxsize > 2 ** 32 else "32"
