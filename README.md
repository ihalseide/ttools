# Ttools

Ttools is a collection of tools for text processing. Feel free to do whatever
you want with all of them!

## Installation

Clone the repository using git, or download an archive file.

## Dependencies

Requires Python 3.

## Usage

General usage is like this: `python3 <script name> <arguments>`

## Squash

squash.py removes whitespace from files

## Textstat

Get general text statistics for a file.

usage: `textstat.py [-h] [-p] file`

```
positional arguments:
  file          input file for analysis

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  specify to pretty-print the stats
```

Note that 'shortest\_line' and 'longest\_line' give line numbers, not actual
lengths!

## Charstat

Get statistics for characters of a text file.

usage: `charstat.py [-h] [-p] file`

```
positional arguments:
  file          input file for analysis

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  specify to pretty-print the stats

Note: Occurence data in pretty printing is in the format 'row:col , index'
```

## Trailstat

Get lines that have trailing whitespace.

usage: `trailstat.py [-h] [-p] file`

```
positional arguments:
  file          input file for analysis

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  specify to pretty-print the stats
```

## Contributing

Feel free to ask, comment, and critique. Also feel free to submit a pull
request if you think you have something useful to contribute!

## License

Please see the 'LICENSE.txt' file for license information.
