#!/usr/bin/python3
"""Module class Base"""
import json
import os.path


class Base():
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method returns JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method writes JSON string
        representation of a list of objects"""
        if list_objs is None:
            list_objs = []
        list_new = []
        with open(f"{cls.__name__}.json", "w") as file:
            for i in list_objs:
                list_new.append(i.to_dictionary())
            list_new = cls.to_json_string(list_new)
            file.write(list_new)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if cls.__name__ == "Square":
            object_dummy = cls(1)
            object_dummy.update(**dictionary)
        else:
            object_dummy = cls(1, 2)
            object_dummy.update(**dictionary)
        return object_dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        ret = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                str_list = file.read()
            dict_list = cls.from_json_string(str_list)
            for obj_dict in dict_list:
                new_obj = cls.create(**obj_dict)
                ret.append(new_obj)
        return ret
