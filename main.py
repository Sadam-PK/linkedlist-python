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

    def at_head(self, new_node):
        temp = self.head
        self.head = new_node
        self.head.next = temp
        del temp

    def display(self):
        current = self.head
        while True:
            if current is None:
                break
            print(current.data)
            current = current.next

    def at_positio(self, new_node, position):
        current = self.head
        current_position = 0
        previous = None
        while True:
            if current_position == position:
                previous.next = new_node
                new_node.next = current
                break
            previous = current
            current = current.next
            current_position += 1


nn = Node('sadam')

linkedlist = LinkedList()
linkedlist.insert(nn)

nn = Node('hamza')
linkedlist.insert(nn)

nn = Node('asad')
linkedlist.insert(nn)

nn = Node('Daud')
linkedlist.at_positio(nn, 1)
linkedlist.display()
