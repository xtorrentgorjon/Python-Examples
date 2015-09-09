#####
# Python Examples:
#        multiprocessing.py
#
# Extremely simple communication between processes.
#
# Xavier Torrent Gorjon
#####

import signal
import time

def signal_handler(n, m):
	print "Wtf just happened?? ("+str(n)+")"


signal.signal(signal.SIGALRM, signal_handler)

signal.alarm(2)

print "Starting sleep."

time.sleep(5)

print "Sleep 1 over."

time.sleep(5)

print "Exiting."
