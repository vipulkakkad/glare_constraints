import os
import sys
import io
import struct

s = sys.stdin.read(15)
if "".join(s) != ">>planar_code<<":
	exit()
print "graph planar {"
print "	concentrate=true"

s = sys.stdin.read(1)
n = ord(s[0])

for x in range(n):
	s = sys.stdin.read(1)
	t = ord(s[0])
	while t != 0:
		sys.stdout.write("	v"+str(x+1))
		sys.stdout.write(" -- v"+str(t))
		print ""
		s = sys.stdin.read(1)
		t = ord(s[0])
	else:
		print ""
print "}"
