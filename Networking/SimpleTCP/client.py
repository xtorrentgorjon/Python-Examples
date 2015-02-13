#####
# Python Examples:
#        client.py
#
# Very simple TCP client.
#
# Xavier Torrent Gorjon
#####

import socket
import struct

# CONSTANTS
ADDR = "127.0.0.1"
PORT = 8005
CONN_ADDR = (ADDR, PORT)

cs = socket.socket()
cs.connect(CONN_ADDR)

while True:
	n = raw_input()
	print len(n), ":", n
	cs.send(n)

cs.close()
