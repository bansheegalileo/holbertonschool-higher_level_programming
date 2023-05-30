#!/usr/bin/python3
"""
    returns an object rep.d by JSON string
"""
import json


def from_json_string(my_str):
    """
        as above
    """
    return json.loads(my_str)
