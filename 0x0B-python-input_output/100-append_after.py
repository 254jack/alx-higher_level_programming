#!/usr/bin/python3
"""100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string
        f.writelines(lines)
