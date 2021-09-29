#!/usr/bin/python3
"""
    100-singly_linked_list
    damn
    return {}
"""


class Node:
    """
        Node
    """
    def __init__(self, data, next_node=None):
        """ arro """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ data """
        return self.__data

    @data.setter
    def data(self, value):
        """ data """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
        SinglyLinkedList
    """
    def __init__(self):
        """ init """
        self.__head = None

    def sorted_insert(self, value):
        """ sorted_insert """
        try:
            node = Node(value, None)
        except TypeError:
            return
        if self.__head is None:
            self.__head = node
        else:
            ptr = self.__head
            if ptr.data > value:
                node.next_node = self.__head
                self.__head = node
                return
            while ptr.next_node is not None:
                if ptr.next_node.data >= value:
                    break
                ptr = ptr.next_node
            node.next_node = ptr.next_node
            ptr.next_node = node

    def __str__(self):
        """ str """
        he = self.__head
        if he is None:
            return ""
        while he.next_node is not None:
            print("{}".format(he.data))
            he = he.next_node
        return str(he.data)
