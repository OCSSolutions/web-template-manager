# Web Template Manager

An open-source, command line tool for working with web templates created by programs like Dreamweaver and Microsoft Expression.  With wtm you can create new HTML files based on DWT (Dreamweaver/Dynamic web templates) files or update existing HTML files that use the template with changes in the master template.

## Installation

#### Debian, Ubuntu, and Linux Mint

```
wget https://github.com/OCSSolutions/web-template-manager/raw/master/web-template-manager.deb
sudo dpkg -i web-template-manager.deb
```

#### All Other Linux Platforms, Mac, and UNIX

```
wget https://raw.githubusercontent.com/OCSSolutions/web-template-manager/master/wtm.py
```

Then copy script to a location of your choice, probably `/usr/local/bin`

#### Windows

Install Python, then download wtm.py via the link above.

## Usage

```
usage: wtm.py [-h] [-c] [-u] input output

positional arguments:
  input         input file
  output        output file

optional arguments:
  -h, --help    show this help message and exit
  -c, --create  Create new HTML File
  -u, --update  Update existing HTML File
```
