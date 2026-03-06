"""
Name: Neel Jhala
Assignment: Project 2, linked.py
Date: 3/4/2026
Summary:
This file creates the node and linked computer classes used to establish the linked structure computer database in 
the main code
"""
from Computer import ComputerSystem
class Node():
    """
    Singular node in a linked structure
    """
    def __init__(self, data, next=None):
        """
        :param data: The data contained by the node
        :param next: The next node in the linked structure
        """
        self.data = data
        self.next = next

class linkedComputer():
    """
    Bag implementation of a linked structure that contains Computer classes as data
    """

    def __init__(self):
        self._items = None
        self._size=0
    
    def __iter__(self):
        """
        Sets up iteration through the linked structure using a cursor that moves through each node and returns its
        data
        """
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
    
    def add(self, computerData):
        """
        Adds a computer to the linked structure, inserting by year purchased
        :param computerData: the computer being added(must be of the computer class)
        """
        newNode = Node(computerData)

        # Insert at head if list is empty or new item belongs before the first node
        if self._items is None or computerData.yearPurchased <= self._items.data.yearPurchased:
            newNode.next = self._items
            self._items = newNode
            self._size += 1
            return

        cursor = self._items
        while cursor.next is not None and cursor.next.data.yearPurchased <= computerData.yearPurchased:
            cursor = cursor.next

        newNode.next = cursor.next
        cursor.next = newNode
        self._size += 1

    
    def remove(self):
        """
        Removes and returns data of the first node in the linked structure(the oldest computer)
        """
        if self._items is None:
            return None

        data = self._items.data
        self._items = self._items.next
        self._size -= 1
        return data
