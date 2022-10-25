#!/usr/bin/python3
"""Add all  arguments to a list and save them to a file"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

with open("add_item.json", 'w', encoding="utf-8") as f:
    f.write(json.dumps(sys.argv[1:]))
