#!/usr/bin/python3
"""Contain a function to add json string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """save json text to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
