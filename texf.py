import re
import os
import sys
import types

date_type = '[\d]+-[\d]+[\d]-[\d]+'
time_type = '[\d]+:[\d]+:[\d]+'
octet_type = '0x[\d]+'

pattern = '^' + date_type + ' ' + time_type + ' DEBUG ' + octet_type + ' - [[' + time_type + '-\d+] (.+$)'

def get_text_file(path):
	f = open ( path,"r")
	data = f.read()
	return data

def tex_filter(pattern, path):
	m = re.findall(pattern, get_text_file(path), re.MULTILINE)
	for _m in m:
		if type(_m) is types.StringType:
			print _m
		else:
			print( (',').join(_m) )

if len(sys.argv) < 2:
	exit('Usage: texf.py FILENAME [PATTERN]')

if len(sys.argv) == 3:
	pattern = sys.argv[2]

filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit('ERROR: file not found(%s)' % filename)


tex_filter( pattern, filename )

