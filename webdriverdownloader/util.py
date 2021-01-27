"""
Module for utility functions.

This code is released under the MIT license.
"""
from cpuinfo import get_cpu_info

def get_architecture_bitness() -> str:
    """
    Function for getting the "bitness" of the underlying architecture i.e. if it is 32-bit or 64-bit.
    :return: The bitness of the underlying architecture, as a str i.e. "32" or "64"
    """
    return str(get_cpu_info()['bits'])
