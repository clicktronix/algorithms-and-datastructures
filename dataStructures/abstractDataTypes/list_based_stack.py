#!/usr/bin/env python
"""List based stack implementation"""
from linked_list import LinkedList


class ListBasedStack:
    """List based stack implementation"""

    def __init__(self):
        self.length = 0
        self.stack = LinkedList()

    def empty(self):
        """Return true if stack is empty"""
        return self.stack.get_length() == 0

    def push(self, element):
        """Add element to the end of the stack"""
        self.stack.append(element)

    def pop(self):
        """Return last element"""
        element = self.stack.last()
        self.stack.remove(element.data)
        self.length -= 1
        return element
