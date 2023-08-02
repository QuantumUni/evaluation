
class ListNode:
    def __init__(self, value=None):
        self._value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None
    
    def __isEmpty(self):
        return self._first == None
    
    def append(self, item):
        node = ListNode(item)
        if(self.__isEmpty()):
            self._first = node
            self._last = node
        else:
            self._last._next = node
            self._last = node 
    
    def prepend(self, item):
        node = ListNode(item)
        if(self.__isEmpty()):
            self._last=self._first =node
        else:
            node._next = self._first
            self._first = node
    
    def removeFirst(self):
        if(self.__isEmpty()):
            print("Linked List is already empty!")
        node = self._first._next
        self._first = node
    
    def removeLast(self):
        previousNode = self.getPreviousNode(self._last)
        self._last = previousNode
        self._last._next = None
    
    def find(self, value):
        if(self.__isEmpty()):
            print("List is Empty!")
            return
        index = 0
        current = self._first
        while(current!=None):
            if(current._value==value):
                return index
            else:
                index+=1
                current = current._next
        return -1

    def reverse(self):
        if self.__isEmpty():
            print("List is Empty!")
            return
        
        previous = self._first
        current = self._first._next

        while(current!=None):
            next = current._next
            current.next = previous
            previous = current
            current = next
        self._last = self._first
        self._last._next = None
        self._first = previous

    def getPreviousNode(self, node):
        current = self._first
        while(current!=None):
            if(current._next==node): return current
            current = current._next
        return None
    

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.append(2)
    linkedList.append(3)
    linkedList.prepend(8)
    linkedList.prepend(3332)
    linkedList.prepend(61)
    linkedList.append(234)
    linkedList.prepend(33)
    linkedList.append(3321)
    linkedList.append(983)
    linkedList.removeFirst()
    linkedList.removeLast()
    index = linkedList.find(3321)
    linkedList.reverse()
    print(index)