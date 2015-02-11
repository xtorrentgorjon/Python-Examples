__author__ = 'sendotux'

import socket
import struct
import threading

# CONSTANTS
DEFAULT_ADDR = "224.55.55.55"
DEFAULT_PORT = 40000
ALL_IP = ""

MCAST_GROUP = (DEFAULT_ADDR, DEFAULT_PORT)
LISTEN_ADDR = (ALL_IP, DEFAULT_PORT)


class MulticastSender(threading.Thread):
    """
    Class that implements a Multicast socket to send data.

    This class features its own execution thread. Information can
    be queued to be sent through the send_data() function.
    """
    def __init__(self, group=MCAST_GROUP):
        """
        Class constructor. Takes a tuple as an option argument
        for the multicast group.
        """
        threading.Thread.__init__(self)
        self.__sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sender_socket.settimeout(0.1)
        ttl = struct.pack('b', 1)
        self.__sender_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        self.__group = group
        self.__sending_queue = []
        self.__active = True

    def run(self):
        """Start the thread execution."""
        while self.__active:
            if len(self.__sending_queue) > 0:
                data = self.__sending_queue.pop(0)
                self.__sender_socket.sendto(data, self.__group)

    def send_data(self, data):
        """Append a new message to be sent on the queue."""
        self.__sending_queue.append(data)

    def close(self):
        """Close the connection, end the thread loop."""
        self.__active = False
        self.__sender_socket.close()


class MulticastReceiver(threading.Thread):
    """
    Class that implements a Multicast socket to receive data.

    This class features its own execution thread. Information received is
    put on a queue that can be accessed through the get_data() function.
    """
    def __init__(self, group=MCAST_GROUP):
        """
        Class constructor. Takes a tuple as an option argument
        for the multicast group.
        """
        threading.Thread.__init__(self)
        self.__listener_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__listener_socket.settimeout(0.1)

        self.__listener_socket.bind(("", group[1]))
        multicast_group = socket.inet_aton(group[0])

        opts = struct.pack('4sL', multicast_group, socket.INADDR_ANY)
        self.__listener_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, opts)

        self.__receiving_queue = []
        self.__active = True

    def run(self):
        """Start the thread execution."""
        while self.__active:
            data = ""
            try:
                data, address = self.__listener_socket.recvfrom(1024)
            except socket.timeout:
                pass
            if data != "":
                self.__receiving_queue.append(data)

    def get_data(self):
        """Get oldest message received."""
        try:
            return self.__receiving_queue.pop(0)
        except IndexError:
            return "Error: Nothing received."

    def close(self):
        """Close the connection, end the thread loop."""
        self.__active = False
        self.__listener_socket.close()


class Multicast(object):
    """Wrapper class that combines both sending and receiving sockets."""
    def __init__(self, group=MCAST_GROUP):
        self.__mc_sender = MulticastSender(group)
        self.__mc_receiver = MulticastReceiver(group)

    def start(self):
        self.__mc_sender.start()
        self.__mc_receiver.start()

    def send_data(self, data):
        self.__mc_sender.send_data(data)

    def get_data(self):
        return self.__mc_receiver.get_data()

    def close_all(self):
        self.__mc_receiver.close()
        self.__mc_sender.close()

if __name__ == "__main__":
        mc = Multicast(("224.66.55.66", 55555))
        mc.start()

        in_string = None
        while in_string != "quit":
            in_string = raw_input()
            in_string1 = in_string.split(" ")
            if in_string1[0] == "send":
                mc.send_data(" ".join(in_string1[1:]))
            elif in_string1[0] == "print":
                print mc.get_data()

        mc.close_all()

