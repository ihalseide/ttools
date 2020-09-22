#!/usr/bin/env python3

import sys
from argparse import ArgumentParser

def squash (filename, output, lines, tabs, spaces, escsingle, escdouble): 
    remove = ''
    if lines:
        remove += '\n'
    if tabs:
        remove += '\t'
    if spaces:
        remove += ' '
        # Non-breaking space
        remove += '\u0020'

    with open(filename, 'r') as f:
        quote1, quote2 = False, False
        for char in f.read():
            if escdouble and not quote1 and char == '"':
                quote2 = not quote2
            if escsingle and not quote2 and char == "'":
                quote1 = not quote1
            if (char not in remove) or (quote1 or quote2):
                print(char, end='', file=output)

def main():
    p = ArgumentParser(description="Remove whitespace")
    p.add_argument('input',
            help='The file to remove linebreaks from')
    p.add_argument('-l', '--lines',
            action="store_true",
            help="Remove line breaks also, CR and LF included")
    p.add_argument('-t', '--tabs',
            action="store_true",
            help="Remove tabs also")
    p.add_argument('-s', '--spaces',
            action="store_true",
            help="Remove spaces also (including non-breaking spaces)")
    p.add_argument('-1', '--single',
            action='store_true',
            help='Preserve space within single quotes')
    p.add_argument('-2', '--double',
            action='store_true',
            help='Preserve space within double quotes')
    args = p.parse_args()

    squash(args.input, sys.stdout, args.lines, args.tabs, args.spaces,
            args.single, args.double)

if __name__ == '__main__':
    main()
