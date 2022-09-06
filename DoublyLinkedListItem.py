"""Doubly Linked List Class."""

Class DoublyLinkedList(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def GetList(self):
        return self.data
    
    def GetNext(self):
        return self.next
        