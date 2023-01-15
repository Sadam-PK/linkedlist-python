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

    def list_length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

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

    def insert_at_any(self, new_node, position):
        if position < 0 or position > self.list_length():
            print('Invalid position.')
            return
        if position == 0:
            self.at_head(new_node)
            return
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

    def delete_end(self):
        previous = None
        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
        del current
        previous.next = None

        # current = self.head
        # last = self.head
        # while True:
        #     if current.next is None:
        #         last.next = None
        #         del last
        #         break
        #     last = current
        #     current = current.next


nn = Node('sadam')

linkedlist = LinkedList()
linkedlist.insert(nn)

nn = Node('hamza')
linkedlist.insert(nn)

nn = Node('asad')
linkedlist.insert(nn)

nn = Node('daud')
linkedlist.insert_at_any(nn, 0)
linkedlist.display()
print('------------')
linkedlist.delete_end()
linkedlist.display()
