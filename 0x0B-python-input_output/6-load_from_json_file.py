#!/usr/bin/python3
"""Contain afunction to deserialize files"""
import json


def load_from_json_file(filename):
    """Create an  object from a file"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
