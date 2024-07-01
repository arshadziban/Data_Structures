class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
linked_list.head.next = second
second.next = third

current = linked_list.head
while current is not None:
    print(current.data)
    current = current.next
