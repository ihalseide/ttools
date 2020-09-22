#!python3

import sys
import argparse

description = "Get statistics for characters of a text file."
epilog = "Note: Occurence data in pretty printing is in the format 'row:col , index'"


def escape(char: str):
    mapping = {
            '\n': r'\n',
            '\t': r'\t'
            }
    return "'" + mapping.get(char, char) + "'"


def location_str(line, column, index):
    return "{: >4}:{: <4}, {: >4}".format(line, column, index)


def print_stats(char_first, char_count, char_last):
    for char in char_first:
        count = char_count[char]
        first_line, first_column, first_index = char_first[char]
        last_line, last_column, last_index = char_last[char]
        pchar = escape(char)
        print(pchar, 
              'count:', count,
              'first_line:', first_line,
              'first_column:', first_column,
              'first_index:', first_index,
              'last_line:', last_line,
              'last_column:', last_column,
              'last_index:', last_index)


def pretty_print_stats(char_first, char_count, char_last, filename=None):
    if filename:
        print("Character stats for \"{}\":".format(filename))
    else:
        print("Character stats:")
    print()
    print("   Char   | Count  | First Ocurrence | Last Ocurrence ")
    print("----------+--------+-----------------+-----------------")
    for char in char_first:
        count = char_count[char]
        first = location_str(*char_first[char])
        last = location_str(*char_last[char])
        pchar = escape(char)
        print(" {: <8} | {: >6} | {} | {}" .format(pchar, count, first, last))
    print()


def read_stats(filename):
    char_count = dict()
    char_first = dict()
    char_last = dict()
    with open(filename, 'r+') as file_in:
        # Keep track of the character index
        index = 0
        # Iterate the lines for memory
        for line_num, line in enumerate(file_in.readlines()):
            # Iterate the chars for each line
            for column, char in enumerate(line):
                # Keep track of the first occurence
                if not char in char_first:
                    char_first[char] = (line_num + 1, column, index)
                    char_count[char] = 0 # will be incremented soon
                # Keep track of last occurence
                char_last[char] = (line_num + 1, column, index)
                # Keep a running total of the occurences of the char
                char_count[char] += 1
                # Inc. index
                index += 1
    return char_first, char_count, char_last


def main():
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    parser.add_argument("file", help="input file for analysis")
    parser.add_argument("-p", "--pretty",
            help="specify to pretty-print the stats",
            action="store_true")
    args = parser.parse_args()

    try:
        stats = read_stats(args.file)
        # Output the results
        if args.pretty:
            pretty_print_stats(*stats, filename=args.file)
        else:
            print_stats(*stats)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

