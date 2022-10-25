#!/usr/bin/python3
"""contain a method to retrieve json serialized object"""
import json


def from_json_string(my_str):
    """Return deserialized object"""
    return json.loads(my_str)
