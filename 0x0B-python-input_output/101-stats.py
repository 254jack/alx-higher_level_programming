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


if __name__ == '__main__':
    from sys import argv, stdin, stderr
    from collections import OrderedDict
    from datetime import datetime

    line_no = 0
    total_file_size = 0
    code_counts = OrderedDict.fromkeys([200, 301, 400, 401, 403,
                                        404, 405, 500], 0)

    try:
        for line in stdin:
            line_no += 1

            a = line.split('-', 1)
            if len(a) != 2:
                continue

            b = a[1].split(']')
            timecode = b[0].lstrip(' [')
            try:
                datetime.strptime(timecode, '%Y-%m-%d %H:%M:%S.%f')
            except:
                stderr.write("{}: {}: invalid timecode\n".format(
                    argv[0], line_no))
                pass

            c = b[1].split('"')
            c = c[1:]
            if c[0] != 'GET /projects/260 HTTP/1.1':
                stderr.write("{}: {}: unexpected HTTP request\n".format(
                    argv[0], line_no))

            d = c[1].lstrip(' ')
            d = d.rstrip('\n')
            d = d.split(' ')

            if d[0].isdecimal():
                code = int(d[0])
                code_counts[code] += 1

            if d[1].isdecimal():
                total_file_size += int(d[1])

            if line_no % 10 == 0:
                print_log_totals(total_file_size, code_counts)
        print_log_totals(total_file_size, code_counts)

    except (KeyboardInterrupt):
        print_log_totals(total_file_size, code_counts)
        raise
