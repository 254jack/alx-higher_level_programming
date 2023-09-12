#!/usr/bin/python3

""" a save_to_json_file module"""
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
       d = json.load(f)
       return (d)
       
