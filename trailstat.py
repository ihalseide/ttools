#!python3

import sys
import argparse

def iterable(x):
    try:
        iter(x)
        return True
    except TypeError:
        return False


def print_stats(stats: dict):
    for key, value in stats.items():
        if iterable(value):
            print(key, ':', sep='')
            if value:
                print(' '.join([str(x) for x in sorted(value)]))
            continue
        print(key, ': ', value, sep='')


def convert_name(s: str):
    return s.replace('_', ' ').capitalize()


def pretty_print_stats(stats: dict, filename=None):
    print()
    if filename is not None:
        header = "Basic text file statistics for \"{}\":".format(filename)
    else:
        header = "Basic text file statistics:"
    print(header)
    print('-' * len(header))
    for key, value in stats.items():
        print(convert_name(key), ': ', value, sep='')
    print()


def read_stats(filename):
    trailing_lines = set()
    total_space = 0

    with open(filename, "r") as data:
        for i, line in enumerate(data.readlines()):
            # Check the line for trailing whitespace
            # Start at the end because that's all that matters
            for char in reversed(line):
                if not char.isspace():
                    break
                if char == '\n':
                    continue
                total_space += 1
                trailing_lines.add(i + 1)

    return {'total_trailing_whitespace': total_space,
            'trailing_lines': trailing_lines}


def main():
    parser = argparse.ArgumentParser(description="Get lines that have trailing whitespace.")
    parser.add_argument("file", help="input file for analysis")
    parser.add_argument("-p", "--pretty",
            help="specify to pretty-print the stats",
            action="store_true")
    args = parser.parse_args()

    try:
        stats = read_stats(args.file)
        # Output the results
        if args.pretty:
            pretty_print_stats(stats, filename=args.file)
        else:
            print_stats(stats)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
