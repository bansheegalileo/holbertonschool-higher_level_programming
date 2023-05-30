#!/usr/bin/python3
"""
    reads a text file and prints to stdout
"""


def read_file(filename=""):
    """
        as above
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
