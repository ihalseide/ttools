#!/usr/bin/env python3

import argparse, sys

# A function that does nothing but return its argument
def pass_fn(x):
    return x

# Create a prompt for use with interactive_template
def title_msg(prompt):
    return str(prompt).title() + ': '

# Fill in a template from user input in stdin
def interactive_template(template: str, msg_func=pass_fn, val_func=pass_fn,
        delimiters='[]'):
    result, skip = '', False
    replace_me = ''
    for i, char in enumerate(template):
        if char == delimiters[0] and not skip:
            # Begin delimiter
            skip = True
            replace_me = ''
            continue
        if char == delimiters[1]:
            # End delimiter
            skip = False
            msg = msg_func(replace_me)
            user = input(msg)
            val = val_func(user)
            result += str(val)
            continue
        if skip:
            # Build message
            replace_me += char
        else:
            # Build literal output
            result += char
    return result
    
# Fill occurrences of text between the delimiters in a template with values
def fill_template(template: str, values: list, delimiters='[]'):
    result, skip = '', False
    vals = iter(values)
    for i, char in enumerate(template):
        if char == delimiters[0] and not skip:
            # Begin delimiter
            skip = True
            continue
        if char == delimiters[1]:
            # End delimiter
            skip = False
            result += str(next(vals))
            continue
        if not skip:
            result += char
    return result

def main():
    # Define program arguments...
    parser = argparse.ArgumentParser(description=
            'Tool for filling in a template string with values.')
    
    parser.add_argument('file', type=open, help='Template file to fill in')
    parser.add_argument('-d', dest='delimiters', default='[]', help='A string of 2 characters that represent the start of a template entry and the end of one. Default is "[]"')

    # Require either values or interactive mode
    g1 = parser.add_mutually_exclusive_group(required=True)
    g1.add_argument('-v', dest='values', action='extend', nargs='+', help='Take any amount of string values to replace into the template with')
    g1.add_argument('-i', dest='interactive', action='store_true', help='Use input (from stdin) to get the values interactively.')

    # Parse the arguments now
    args = parser.parse_args()

    # Use stdin for template if template not given
    template = args.file.read()

    # Perform template filling
    if args.interactive:
        s = interactive_template(template, title_msg, pass_fn, args.delimiters)
    else:
        s = fill_template(template, args.values, args.delimiters)

    # Output result
    print(s)

if __name__ == '__main__':
    main()
