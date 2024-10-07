import os
os.system("clear")

class Node:
    def __init__(self,v,n = None):
        self.value = v
        self.next = n
class Linked_List:
    def __init__(self):
        self.head = None
    def insertStart(self,data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    def insertIndex(self,data,index):
        node = Node(data)
        h = self.head
        pos = 0
        if pos == index:
            self.insertStart(data)
        else:
            while h != None and pos + 1 != index:
                pos += 1
                h = h.next
            if h is not None:
                node.next = h.next
                h.next = node
            else:
                print('Index not present')
    def insertEnd(self,data):
        node = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = node
    def show(self):
        h = self.head
        ls = []
        while h:
            ls.append(h.value)
            h = h.next
        return ls
    def print(self):
        h = self.head
        while h:
            print(h.value, end = ' -> ')
            h = h.next
        print('None')

ll = Linked_List()
print(ll.show())
ll.print()
ll.insertStart('A')
ll.insertStart('B')
ll.insertEnd('C')
ll.insertIndex('D',1)
print(ll.show())
ll.print()