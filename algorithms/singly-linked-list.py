# head, tail, length
class Node:
    def __init__(self, element):
        self.value = element
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, element):
        node = Node(element)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self
