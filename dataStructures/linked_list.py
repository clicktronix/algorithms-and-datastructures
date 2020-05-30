#!/usr/bin/env python
"""Linked list Implementation"""


class Node:
    """Linked list's node Implementation"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    """Linked list Implementation"""

    def __init__(self):
        self.length = 0
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, data):
        """It takes an item of data as an argument and puts it at the beginning of the list"""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1
