#!/usr/bin/python3
"""Analyzes and displays statistics based on input data.

Reads from standard input and computes metrics.
After every ten lines or when a keyboard interruption 
(CTRL + C) occurs, it prints various statistics:
    - Accumulated total file size.
    - Count of read status codes.

"""

def display_metrics(total_file_size, status_code_count):
    """Function displays accumulated metrics.

    Args:
        total_file_size (int): The total size of the files read.
        status_code_count (dict): Dictionary of accumulated status 
	code counts.
    """
    print("Total file size: {}".format(total_file_size))
    for key in sorted(status_code_count):
        print("{}: {}".format(key, status_code_count[key]))

if __name__ == "__main__":
    import sys

    total_file_size = 0
    status_code_count = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                display_metrics(total_file_size, status_code_count)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                total_file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_status_codes:
                    if line[-2] not in status_code_count:
                        status_code_count[line[-2]] = 1
                    else:
                        status_code_count[line[-2]] += 1
            except IndexError:
                pass

        display_metrics(total_file_size, status_code_count)

    except KeyboardInterrupt:
        display_metrics(total_file_size, status_code_count)
        raise
