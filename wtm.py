#!/usr/bin/env python

# Web Template Manager Version 1.00
# Copyright (C) 2016 OCS Solutions, Inc. All Rights Reserved.
# Licensed under the GPLv3
# For more information, please see https://github.com/OCSSolutions/web-template-manager

WTM_VERSION = "1.00"

import argparse
import re
import os
import sys
import random

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        print "Web Template Manager Version " + WTM_VERSION
        print "A tool for managing web templates on the command line."
        print "Copyright (C) 2016 OCS Solutions, Inc.  All Rights Reserved."
        print "Licensed under the GPLv3.  For more info, please see:"
        print "https://github.com/OCSSolutions/web-template-manager"
        print
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        print
        sys.exit(2)

parser = MyParser()
parser.add_argument("input", help="input file")
parser.add_argument("output", help="output file")
parser.add_argument("-c", "--create", help="Create new HTML File", action='store_true')
parser.add_argument("-u", "--update", help="Update existing HTML File", action='store_true')
args = parser.parse_args()

def create(infile, outfile):
	fw = open(outfile, 'w+')
	with open(infile, 'r') as fp:
		for line in fp:
			fw.write(line)

	fw.close()

def update(infile, outfile):
	fr = open(infile, 'r')
	fpr = open(outfile, 'r')
	temp = 'temp' + str(random.random())
	print (temp)
	fw = open(temp, 'w+')

	start = re.compile('.*\\bInstanceBeginEditable\\b.*')
	end = re.compile('.*\\bInstanceEndEditable\\b.*')
	STATE = 0
	for line in fr:
		if line[:4] == '<!--':
			if start.match(line):
				STATE = 1
			elif end.match(line):
				STATE = 0

		if STATE == 0:
			fw.write(line)

		elif STATE == 1:
			rline = fpr.readline()
			rline = fpr.readline()
			while start.match(rline) == None and len(rline) > 0:
				rline = fpr.readline()

			fw.write(rline)
			rline = fpr.readline()
			while end.match(rline) == None and len(rline) > 0:
				fw.write(rline)
				rline = fpr.readline()
			
			STATE = 2
	fw.close()
	fpr.close()
	fr.close()
	os.remove(outfile)
	os.rename(temp, outfile)

if args.create == True:
	create(args.input, args.output)
else:
	update(args.input, args.output)	
