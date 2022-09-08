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
            self.last.setNext(newNode)
            newNode.setPrev(self.last)
            newNode.setNext(self.first)
            self.first.setPrev(newNode)
            self.last = newNode
            self.cant = self.cant + 1
            print("Node added")

    def is_empty(self):
        return self.cant == 0

    def AddAfter(self,oldItem,data):
        if self.get(self.contains(data)) == self.last:
            self.AddLast(oldItem)
        elif self.get(self.contains(data)) == self.first or self.is_empty():
            self.AddFirst(oldItem)
        else:
            newNode = DoublyLinkedListItem(data)
            search: DoublyLinkedListItem = self.first
            aux: DoublyLinkedListItem = None
            indexData = self.contains(data)
            if indexData != -1:
                aux = self.get(indexData)
                current: DoublyLinkedListItem = aux.GetNext()
                aux.setNext(newNode)
                newNode.setPrev(aux)
                newNode.setNext(current)
                current.setPrev(newNode)
                self.cant = self.cant + 1
                print("Node added")

    def AddBefore(self,beforeItem,data):
        if self.get(self.contains(data)) == self.last:
            self.AddLast(beforeItem)
        
        elif self.get(self.contains(data)) == self.first or self.is_empty():
            self.AddFirst(beforeItem)
        
        else:
            newNode = DoublyLinkedListItem(beforeItem)
            search: DoublyLinkedListItem = self.first
            aux: DoublyLinkedListItem = None
            indexData = self.contains(data)
            if indexData != -1:
                aux = self.get(indexData)
                current: DoublyLinkedListItem = aux.GetPrev()
                aux.setPrev(newNode)
                newNode.setNext(aux)
                newNode.setPrev(current)
                current.setNext(newNode)
                self.cant = self.cant + 1
                print("Node added")

    def Clear(self) -> bool:

        if not self.is_empty():
            self.first = None
            self.last = None
            self.cant = 0
            print("List cleaned")
        else:
            return False

    def contains(self, data) -> int:
        search: DoublyLinkedListItem = self.first
        index = 0
        while search != None:
            if search.GetData() == data:
                return index
            else:
                search = search.GetNext()
                index = index + 1
        return -1
    
    def get(self, index) -> DoublyLinkedListItem:
        if index >= 0 and index < self.cant:
            search: DoublyLinkedListItem = self.first
            for i in range(index):
                search = search.GetNext()
            return search
        else:
            return None
    
    def Remove(self, data) -> bool:

        current: DoublyLinkedListItem = self.first
        delete: DoublyLinkedListItem = None
        if self.first.GetData() == data:
            self.last.setNext(self.first.GetNext())
            self.first.GetNext().setPrev(self.last)
            self.first = self.first.GetNext()
            self.cant = self.cant - 1
            return True
        
        if self.last.GetData() == data:
            self.first.setPrev(self.last.GetPrev())
            self.last.GetPrev().setNext(self.first)
            self.last = self.last.GetPrev()
            self.cant = self.cant - 1
            return True
        
        delete = self.get(self.contains(data))

        if delete != None:
            delete.GetPrev().setNext(delete.GetNext())
            delete.GetNext().setPrev(delete.GetPrev())
            self.cant = self.cant - 1
            return True
        else:
            return False

    def RemoveFirst(self) -> bool:
        if not self.is_empty():
            self.first = self.first.GetNext()
            self.first.setPrev(self.last)
            self.last.setNext(self.first)
            self.cant = self.cant - 1
            return True
        else:
            return False

    def RemoveLast(self) -> bool:
        if not self.is_empty():
            self.last = self.last.GetPrev()
            self.last.setNext(self.first)
            self.first.setPrev(self.last)
            self.cant = self.cant - 1
            return True
        else:
            return False
        