"""Doubly Linked List Class."""
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

class DoublyLinkedListItem(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def GetList(DoublyLinkedList):
        if DoublyLinkedList.next == None:
            return DoublyLinkedList.item
        else:
            return DoublyLinkedList.item + " " + DoublyLinkedListItem.GetList(DoublyLinkedList.next)
    
    def GetData(self):
        return self.data

    def GetNext(self):
        return self.next
    
    def GetPrev(self):
        return self.prev
    
    def setNext(self, node):
        self.next = node
    
    def setPrev(self, node):
        self.prev = node