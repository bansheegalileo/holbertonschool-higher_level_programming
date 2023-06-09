#!/usr/bin/python3
"""
    creates Object from JSON file
"""
import json


def load_from_json_file(filename):
    """
        as above
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
