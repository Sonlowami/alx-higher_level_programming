#!/usr/bin/python3
"""Contain a base class"""
import json
import csv


class Base:
    """Contain some methods"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize objects of type Base"""
        self.id = 0
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return the json string representation of a dictionary"""
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs=[]):
        """Save the list objects to file"""
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as f:
            if not list_objs:
                f.write("")
                return
            for obj in list_objs:
                f.write(cls.to_json_string(obj.to_dictionary()))

    def from_json_string(json_string):
        """Deserialize a json string"""
        if not json_string:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from a dictionary of attributes"""
        x = cls(1, 1, 1, 1, 1)
        x.update(**dictionary)
        return x

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list_obj to a csv file"""
        with open(f"{cls.__name__}.csv", 'w', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(list_objs)

