#!/usr/bin/python3
"""
    writes str to text file and returns num of chars
"""


def write_file(filename="", text=""):
    """
        as above
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
