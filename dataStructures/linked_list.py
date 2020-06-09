#!/usr/bin/env python
"""Linked list Implementation"""


class Node:
    """Linked list's node implementation"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)


class LinkedList:
    """Linked list implementation"""

    def __init__(self):
        self.length = 0
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_length(self):
        """Return list length"""
        return self.length

    def add_first(self, data):
        """It takes an item of data as an argument and puts it at the beginning of the list"""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert_at_end(self, data):
        """Add element to the end of list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def insert_after(self, before_data, data):
        """Insert element after passed"""
        node = self.head
        while node is not None:
            if node.item == before_data:
                break
            node = node.next
        if node is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1

    def insert_to_beginning(self, data):
        """Add element to the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def remove_node(self, remove_data):
        """Remove element from the list"""
        head = self.head
        if head is not None and head.data == remove_data:
            self.head = head.next
            self.length -= 1
            head = None
            return
        while head is not None:
            if head.data == remove_data:
                break
            prev = head
            head = head.next
        if head is None:
            return
        prev.next = head.next
        self.length -= 1
        head = None

    def traverse(self):
        """Print the linked list"""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
