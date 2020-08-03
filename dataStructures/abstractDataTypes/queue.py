#!/usr/bin/env python
"""Queue implementation"""
from baseDataTypes.linked_list import LinkedList


class Queue:
    """Queue implementation"""

    def __init__(self):
        self.length = 0
        self.queue = LinkedList()

    def empty(self):
        """Returns true if queue is empty"""
        return self.queue.length == 0

    def push(self, element):
        """Add element to the end of the queue"""
        self.queue.append(element)

    def pop(self):
        """Returns first element"""
        element = self.queue.first()
        self.queue.remove(element.data)
        self.length -= 1
        return element
