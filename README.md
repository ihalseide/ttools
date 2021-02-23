# T-Tools

T-Tools stands for text tools. It is my collection of scripts/tools for text file processing. Feel free to do whatever you want with all of them!

## List of Tools

There is a separate readme file and Python script for each tool. The following is the list of tools in alphabetical order:

* charstat.py

* paginate.py

* squash.py

* template.py

* textstat.py

* trailstat.py

## Installation

Clone the repository using git, or download an archive file. The Git repository is hosted at "https://github.com/ihalseide/ttools.git".

## Dependencies

Requires Python 3.

## License

Please see the file named 'LICENSE.txt'.

## Individual Tool Descriptions

The rest of this file contains the descriptions of each text tool.

### T-Tools: charstat

```
usage: charstat.py [-h] [-p] file
```

Get statistics for characters of a text file.

positional arguments:
  file          input file for analysis

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  specify to pretty-print the stats

Note: Occurence data in pretty printing is in the format 'row:col , index'

### T-Tools: squash

```
usage: squash.py [-h] [-l] [-t] [-s] [-1] [-2] input

Remove whitespace

positional arguments:
  input         The file to remove linebreaks from

optional arguments:
  -h, --help    show this help message and exit
  -l, --lines   Remove line breaks also, CR and LF included
  -t, --tabs    Remove tabs also
  -s, --spaces  Remove spaces also (including non-breaking spaces)
  -1, --single  Preserve space within single quotes
  -2, --double  Preserve space within double quotes
```

### Template tool

Usage: `template.py`

There are no command line arguments, since the script is interactive.

### T-Tools: textstat

```
usage: textstat.py [-h] [-p] file

Get general text statistics for a file.

positional arguments:
  file          input file for analysis

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  specify to pretty-print the stats
```

### T-Tools: Trailstat

```
usage: trailstat.py [-h] [-p] file

Get info on lines that have trailing whitespace.

positional arguments:
  file          input file for analysis

optional arguments:
  -h, --help    show this help message and exit
  -p, --pretty  specify to pretty-print the stats
```

