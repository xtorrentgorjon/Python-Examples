#####
# Python Examples:
#        threads.py
#
# Simple threading example.
#
# Xavier Torrent Gorjon
#####
import threading

THREAD_NUMBER = 4

class thread_class(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__n = 0
	def run(self):
		n = self.__n
		while n < 1000:
			n+=1
		print self.name, n

if __name__ == "__main__":
	thread_list = []
	for i in range(THREAD_NUMBER):
		thread_list.append(thread_class())
	for i in thread_list:
		i.start()

