#!/usr/bin/env python3

# Fill in a template from user input
def interactive_template (template: str, delimiters='[]'):
    result = ''
    skip = False
    replace_me = ''
    for i, char in enumerate(template):
        if char == delimiters[0] and not skip:
            # Begin delimiter
            skip = True
            replace_me = ''
        elif char == delimiters[1]:
            # End delimiter
            skip = False
            msg = replace_me.title() + ': '
            user = input(msg)
            result += user
        elif skip:
            # Build message
            replace_me += char
        else:
            # Build literal output
            result += char
    return result
    
# Fill occurrences of text between the delimiters in a template with values
# Unused
def fill_template (template: str, values: list, delimiters='[]'):
    result, skip = '', False
    vals = iter(values)
    for i, char in enumerate(template):
        if char == delimiters[0] and not skip:
            # Begin delimiter
            skip = True
        elif char == delimiters[1]:
            # End delimiter
            skip = False
            result += str(next(vals))
        elif not skip:
            # Build normal output
            result += char
    return result

def main ():
    template = input("Enter the name of the file to use as a template\n")
    try:
        with open(template) as t_file:
            delimiters = input("Enter the pair of delimiters to use for the template (e.g [], (), {}, or <>)\n")
            print('Begin filling the template "%s":' % template)
            result = interactive_template(t_file.read(), delimiters)
            print(result)
    except IOError as e:
        print('Error opening file "%s".' % template, e)
    input('Press ENTER or Ctrl-C to exit...')

if __name__ == '__main__':
    main()
