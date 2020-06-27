#!/usr/bin/env python
"""Queue implementation"""
from baseDataTypes import linked_list


class Queue:
    """Queue implementation"""

    def __init__(self):
        self.length = 0
        self.stack = linked_list.LinkedList()

    def empty(self):
        """Returns true if queue is empty"""
        return self.stack.length == 0

    def push(self, element):
        """Add element to the end of the stack"""
        self.stack.append(element)

    def pop(self):
        """Returns first element"""
        element = self.stack.first()
        self.stack.remove(element.data)
        self.length -= 1
        return element
