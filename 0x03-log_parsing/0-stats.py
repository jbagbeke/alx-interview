#!/usr/bin/python3
"""
Log parsing from stdin
"""
import signal
import sys
import re


log_pattern = r'(.*?)\s-\s\[(.*?)\]\s"(.*?)"\s(\d{3})\s(.*?)\Z'
total_file_size = 0
status_code_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}
line_counter = 0


def handle_size_status_code(status_code):
    """
    Converts status code to and file size to int
    """
    try:
        return int(status_code)
    except ValueError:
        return None


# Printing log stat function
def print_log_statistics():
    """
    Prints log statistics with format - <status code>: <number>
    """
    print("File size: {}".format(total_file_size))

    for stat_code in sorted(status_code_count.keys()):
        if status_code_count[stat_code] > 0:
            print("{}: {}".format(stat_code, status_code_count[stat_code]))


try:
    for log_input in sys.stdin:
        log_match = re.match(log_pattern, log_input.strip('\n'))

        if log_match:
            status_code = handle_size_status_code(log_match.group(4))
            file_size = handle_size_status_code(log_match.group(5))

            # Valid status code and file Size
            if status_code and file_size:
                total_file_size += file_size
                status_code_count[str(status_code)] += 1
            line_counter += 1

        if line_counter == 10:
            print_log_statistics()
            line_counter = 0
    print_log_statistics()
except KeyboardInterrupt:
    print_log_statistics()
    raise
