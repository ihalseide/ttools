#!/usr/bin/env python3

import sys
import argparse


def print_stats(stats: dict):
    for key, value in stats.items():
        print(key, value)


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
        if value == True:
            value = 'yes'
        elif value == False:
            value = 'no'
        print(convert_name(key), ': ', value, sep='')
    print()


def read_stats(filename):
    longest_line = 0
    longest_length = None

    shortest_line = 0
    shortest_length = None

    char_count = 0
    line_count = 0
    num_blank_lines = 0
    word_count = 0

    with open(filename, "r") as data:
        for i, line in enumerate(data.readlines()):
            line_count += 1
            length = len(line)
            char_count += length
            word_count += len(line.split())
            # Count blank lines
            if line.isspace():
                num_blank_lines += 1
            else:
                # Only count the length of non-blank lines
                if shortest_length is None or length < shortest_length:
                    shortest_line = i
                    shortest_length = length
                if longest_length is None or length > longest_length:
                    longest_line = i
                    longest_length = length

    ends_with_newline = (line == '\n')

    return { 'character_count': char_count,
            'word_count': word_count,
            'line_count': line_count,
            'shortest_line': shortest_line + 1,
            'longest_line': longest_line + 1,
            'empty_line_count': num_blank_lines,
            'ends_with_newline': ends_with_newline }


def main():
    parser = argparse.ArgumentParser(description="Get general text statistics for a file.")
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
