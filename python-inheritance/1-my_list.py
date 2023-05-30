#!/usr/bin/python3
"""
    Inherit list module
"""


class MyList(list):
    """
        MyList
    """
    def print_sorted(self):
        """
            Print sorted List
        """
        print(sorted(self))
