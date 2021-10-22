import random


class Node:
    def __init__(self, element):
        self.value = element
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return self
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left == None:
                        current.left = node
                        return self
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right == None:
                        current.right = node
                        return self
                    else:
                        current = current.right
                else:
                    return None

    def search(self, term):
        if self.root == None:
            return None
        current = self.root
        while current != None and current.value != None:
            if term == current.value:
                return current.value
            elif term < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def peek(self):
        return self


tree = BinarySearchTree()
for i in range(100):
    tree.insert(random.randint(1, 1000))
item = tree.search(7)
print(item)
item = tree.search(17)
print(item)
item = tree.search(5)
print(item)
item = tree.search(10)
print(item)
