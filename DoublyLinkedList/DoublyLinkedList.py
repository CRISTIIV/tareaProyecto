from DoublyLinkedListItem.DoublyLinkedListItem import DoublyLinkedListItem

class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.first = None
        self.last = None
        self.cant = 0

    def AddFirst(self,data):
        if self.first == None:
            newNode = DoublyLinkedListItem(data)
            self.first = newNode
            self.last = newNode
            self.first.setNext(self.last)
            self.last.setPrev(self.last)
            self.last.setNext(self.first)
            self.last.setPrev(self.first)
            self.cant = self.cant + 1
            print("Node added")
        else:
            newNode = DoublyLinkedListItem(data)
            newNode.setNext(self.first)
            newNode.setPrev(self.last)
            self.first.setPrev(newNode)
            self.last.setNext(newNode)
            self.first = newNode
            self.cant = self.cant + 1
            print("Node added")
        """
        newNode = DoublyLinkedListItem(data)
        newNode.next = self.next
        self.next.prev = newNode
        self.next = newNode
        """

    def AddLast(self, data):
        if self.next == None:
            newNode = DoublyLinkedListItem(data)
            self.next = newNode
            return
        n = self.next
        while n.nref != None:
            n = n.nref
        newNode = DoublyLinkedListItem(data)
        n.nref = newNode
        newNode.prev = n

    def AddAfter(self,newItem,data):
        if self.next == None:
            print("The list is empty")
            return
        else:
            n = self.next
            while n != None:
                if n.item == newItem:
                    break
                n = n.nref
            if n == None:
                print("The item not in the list")
            else:
                newNode = DoublyLinkedListItem(data)
                newNode.prev = n
                newNode.nref = n.nref
                if n.nref != None:
                    n.nref.prev = newNode
                n.nref = newNode

    def AddBefore(self,newItem,data):
        if self.next == None:
            print("The list is empty")
            return
        else:
            n = self.next
            while n != None:
                if n.item == newItem:
                    break
                n = n.nref
            if n == None:
                print("The item is not in the list")
            else:
                newNode = DoublyLinkedListItem(data)
                newNode.nref = n
                newNode.prev = n.prev
                if n.prev != None:
                    n.prev.nref = newNode
                n.prev = newNode

    