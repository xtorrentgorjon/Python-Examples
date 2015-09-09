#####
# Python Examples:
#        linked_list.py
#
# Linked list implementation in Python.
#
# Xavier Torrent Gorjon
#####

class Element(object):
    """Class that represents nodes on the linked list."""
    def __init__(self, data):
        """Class constructor. Sets the data variable."""
        self.__data = data
        self.__next = None

    # Getters and setters.
    def set_data(self, data):
        self.__data = data

    def set_next(self, next_element):
        self.__next = next_element

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    # Function overloads.
    def __str__(self):
        return str(self.__data)


class LinkedList(object):
    """Class that represents a linked list of elements."""
    def __init__(self):
        """Class constructor. List starts with no elements."""
        self.__list = None
        self.__length = 0

    def add(self, data, add_pos=None):
        """
        Adds a new element to the list on the add_pos position.
        If no value is provided for add_pos, it appends the element to the last one.
        """
        node = Element(data)
        if add_pos is None:
            add_pos = self.__length
        if self.__list is None:
            self.__list = node
        else:
            if add_pos == 0:
                node.set_next(self.__list)
                self.__list = node
            else:
                current = self.__list
                current_pos = 1
                while current.get_next() is not None and current_pos < add_pos:
                    current = current.get_next()
                    current_pos += 1
                node.set_next(current.get_next())
                current.set_next(node)
        self.__length += 1

    def delete(self, del_pos=None):
        """
        Deletes the element of the list on the del_pos position.
        If no value is provided for del_pos, it deletes the last one.
        """
        if del_pos is None:
            del_pos = self.__length
        if self.__list is None:
            print "Nothing to remove."
        else:
            if del_pos == 0:
                self.__list = self.__list.get_next()
            else:
                prior = self.__list
                current = self.__list.get_next()
                current_pos = 1
                while current.get_next() is not None and current_pos < del_pos:
                    prior = current
                    current = current.get_next()
                    current_pos += 1
                prior.set_next(current.get_next())
            self.__length -= 1

    # Function overloads.
    def __iter__(self):
        current = self.__list
        while current is not None:
            yield current
            current = current.get_next()

    def __str__(self):
        string = "{"
        count = 0
        for element in self:
            string += str(element)
            count += 1
            if count < self.get_length():
                string += ","
        string += "}"
        return "Number of elements: " + str(self.__length) + ", Values: " + string

    # Getters and setters.
    def get_length(self):
        return self.__length


if __name__ == "__main__":
    n = LinkedList()
    n.add("aaa")
    n.add("bbb")
    n.add("ccc")
    n.add("333")
    n.add("666")
    n.add("999")
    n.add("1")
    n.delete(3)
    print n
