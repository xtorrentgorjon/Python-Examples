__author__ = 'sendotux'

import socket #65536
import struct

# CONSTANTS
ADDR = "127.0.0.1"
PORT = 8005
BIND_ADDR = (ADDR, PORT)

ss = socket.socket()
ss.bind(BIND_ADDR)
ss.listen(1)
conn, addr = ss.accept()

while True:

	a = conn.recv(100)
	print len(a), ":", a

	if a == "quit":
		break

conn.close()
ss.close()
