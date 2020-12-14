#!/usr/local/bin/python3
"""
import platform
print(dir(platform))
print(help(platform))
"""
import platform
print(platform.system())
print(f"This is {platform.system()}")
print(f"The python version is {platform.python_version()}")
print(f"The python version in the form of tuple is {platform.python_version_tuple()}")
print(f"The uname is {platform.uname()}")


