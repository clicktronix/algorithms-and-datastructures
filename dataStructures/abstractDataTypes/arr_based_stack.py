#!/usr/bin/env python
"""Array based stack implementation"""


class ArrBasedStack:
    """Array based stack implementation"""

    def __init__(self):
        self.stack = []

    def empty(self):
        """Return true if stack is empty"""
        return len(self.stack) == 0

    def push(self, element):
        """Add element to the end of the stack"""
        self.stack.append(element)

    def pop(self):
        """Return last element"""
        return self.stack.pop()
