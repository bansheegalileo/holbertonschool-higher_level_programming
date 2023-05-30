#!/usr/bin/python3
"""
    appd.s str at end of txt file and returns num of chars
"""


def append_write(filename="", text=""):
    """
        as above
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
