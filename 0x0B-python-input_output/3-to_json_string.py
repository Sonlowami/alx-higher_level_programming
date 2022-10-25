#!/usr/bin/python3
"""Contain one method to return a json serialized string"""
import json


def to_json_string(my_obj):
    """return a json string representing object"""
    return json.dumps(my_obj)
