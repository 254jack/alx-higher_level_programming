#!/usr/bin/python3
"""
101-stats module
"""


def print_log_totals(total_file_size, code_counts):
    """
    a function that reads stdin line by line and computes metrics
    """
    print("File size: {}".format(total_file_size))
    for code in code_counts:
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))
