import os
import sys

key = 0

m = {}

def _map(path, key_pos):
	f = open ( path,"r")
	for samp in f:
		l = samp.split(',')
		key_name = l[key_pos].strip()
		for i in range(len(l)):

			if i == key_pos:
				continue;
			try:
				m[key_name].append(l[i])
			except Exception, e:
				m[key_name] = [l[i]]

	for k, row in m.iteritems():
		print ('{0},{1}'.format( k, ','.join(row) ) )



if len(sys.argv) < 2:
	exit('Usage: map.py <csv-name> [KEY_POSITION=0]')

if len(sys.argv) == 3:
	key = int(sys.argv[2])

filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit('ERROR: file not found(%s)' % filename)

_map(filename, key)