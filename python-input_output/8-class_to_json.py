#!/usr/bin/python3
"""
    returns description for JSON serialization of an object
"""


def class_to_json(obj):
    """
        as above
    """
    return(obj.__dict__)
