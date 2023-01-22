#!/usr/bin/python3
"""Create a Singly LinkedList in Python"""

class Node:
    """Create structure of a singly linkedlist"""

    def __init__(self, data, next_node=None):
        """Construct a node object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property to retrieve data from a node"""
        return self.__data

    @property
    def next_node(self):
        """Property to retrieve the next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Change the value in data field"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Change the value of next_node"""
        if not isinstance(value, Node) or not isinstance(value, NoneType):
            raise TypeError('next_node must be a Node object')
        self.__node = value


class SinglyLinkedList:
    """Create a singly linkedlist"""

    def __init__(self):
        """Simple initializer"""
        self.__head = Node()

