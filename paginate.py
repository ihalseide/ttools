#!/usr/bin/env python3

description = '''
Split an input file into pages based on line and character counts per page.
A separator value can be used to print in between each page. Emits all output to stdout.
'''


def paginate (file, max_page_lines=10, max_page_chars=1000, max_page_num=None):
    pages = []
    page = ''

    if max_page_num is None:
        # Intentional infinite loop because there is no maximum
        loop = iter(int, None)
    else:
        loop = range(int(max_page_num))

    for _ in loop:
        page += file.read(max_page_chars - len(page))
        if not page:
            # Loop exit point
            break 

        num_lines = 0
        next_read = False
        for index, char in enumerate(page):
            if char != '\n':
                continue
            num_lines += 1
            if num_lines > max_page_lines:
                pages.append(page[:index])
                page = page[index:]
                next_read = True
                # Stop checking for newlines
                break

        # Keep the page data for the next time around
        # since the page was split because of line count
        if next_read:
            continue

        pages.append(page)
        page = ''

    return pages


def main ():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file', help="input file to paginate")
    parser.add_argument('-l', '--lines', default=20, help="page line limit")
    parser.add_argument('-c', '--chars', default=1024, help="page character limit")
    parser.add_argument('-n', '--number', default=None, help="maximum number of pages to generate")
    parser.add_argument('-s', '--separator', default='\0', help="separator string between pages")
    args = parser.parse_args()

    # Allow use of escape codes
    sval = str(args.separator)
    sval = sval.replace('\\0', '\0')
    sval = sval.replace('\\n', '\n')
    sval = sval.replace('\\r', '\r')
    sval = sval.replace('\\t', '\t')
    sval = sval.replace('\\a', '\a')
    sval = sval.replace('\\b', '\b')

    with open(args.file, 'r') as file_in:
        pages = paginate(file_in, int(args.lines), int(args.chars), max_page_num=args.number)

    print(sval.join(pages))


if __name__ == '__main__':
    import argparse
    main()
