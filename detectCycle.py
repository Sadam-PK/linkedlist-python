from main import LinkedList, Node


class NewNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.isVisited = False


def detect_cycle(linkedlist):
    current = linkedlist.head
    current.isVisited = True
    while True:
        if current.next.isVisited is True:
            current.next = None
            break
        current = current.next
        current.isVisited = True


nn_1 = NewNode('Jhon')
nn_2 = NewNode('Ben')
nn_3 = NewNode('Methews')

linkedlist = LinkedList()
linkedlist.insert(nn_1)
linkedlist.insert(nn_2)
linkedlist.insert(nn_3)
nn_3.next = nn_2
detect_cycle(linkedlist)
linkedlist.display()
