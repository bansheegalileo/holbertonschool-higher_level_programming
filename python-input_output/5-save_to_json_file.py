#!/usr/bin/python3
"""
    writes object to text file as JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
        as above
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
