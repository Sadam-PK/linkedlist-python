class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            tail = self.head
            while True:
                if tail.next is None:
                    break
                tail = tail.next
            tail.next = new_node

    def display(self):
        current = self.head
        while True:
            if current is None:
                break
            print(current.data)
            current = current.next


nn = Node('sadam')

linkedlist = LinkedList()
linkedlist.insert(nn)

nn1 = Node('hamza')
linkedlist.insert(nn1)

nn2 = Node('asad')
linkedlist.insert(nn2)

linkedlist.display()
