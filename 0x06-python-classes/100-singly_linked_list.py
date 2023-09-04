#!/usr/bin/python3
""" Singly Linked List """


class Node:
    """ Node class
        - this class creates a node
    """
    def __init__(self, data, next_node=None):
        """Instantiation next_node and data

        Args:
            data (int): an integer value added to node
            next_node (Node, optional): a future node. Defaults to None.
        """
        if type(data) != int:
            raise TypeError('data must be an integer')

        self.__data = data

        if next_node is not None and type(next_node) is not Node:
            raise TypeError('next_node must be a Node object')

        self.__next_node = next_node

    @property
    def data(self):
        """data getter

        Returns:
            integer: the value of the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter

        Args:
            value (int): it returns an integer

        Raises:
            TypeError: raises type error if not integer
        """

        if type(self.__data) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """node getter

        Returns:
            Node: returns the future node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter

        Args:
            value (Node): a Node type node to be set as the future node

        Raises:
            TypeError: raises if not node type
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list creation class """
    def __init__(self):
        """ Instantiation of the main Node """
        self.__head = None

    def sorted_insert(self, value):
        """sort the nodes

        Args:
            value (int): an integer value to be sorted and added to the node
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            temp = self.__head
            jn = Node(value)

            if temp.data > jn.data:
                jn.next_node = temp
                self.__head = jn
            else:
                while temp.next_node is not None:
                    if jn.data < temp.next_node.data:
                        jn.next_node = temp.next_node
                        temp.next_node = jn
                        return
                    temp = temp.next_node
                temp.next_node = jn

    def __str__(self):
        """ string representation of the singly linked list

        Returns:
            string: a list of string data of the nodes
        """
        temp = self.__head
        string = ""

        while temp is not None:
            string += str(temp.data)

            if temp.next_node is not None:
                string += '\n'
            temp = temp.next_node

        return string
