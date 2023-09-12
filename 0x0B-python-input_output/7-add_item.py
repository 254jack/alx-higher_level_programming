#!/usr/bin/python3

""" add_item module """
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

av_edit = argv[1:]

try:
    content_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    content_list = []
finally:
    for arg in av_edit:
        content_list.append(arg)
    save_to_json_file(content_list, "add_item.json")
