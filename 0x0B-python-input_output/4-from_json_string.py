#!/usr/bin/python3
import json
""" from_json_string module"""


def from_json_string(my_str):
    """ a fucntion that returns an object represented by a json string"""
    return json.loads(my_str)
