from main import Node, LinkedList


def swap_next(linkedlist, previous, largest, next_node):
    largest.next = next_node.next
    next_node.next = largest
    if largest is linkedlist.head:
        linkedlist.head = next_node
        return
    previous.next = next_node


def sort(linkedlist):
    # iterations depend on no. of nodes
    iterations = linkedlist.list_length() - 1
    while iterations != 0:
        largest = linkedlist.head
        previous = None
        comparisions = iterations
        while comparisions != 0:
            if largest.data > largest.next.data:
                swap_next(linkedlist, previous, largest, largest.next)
            else:
                previous = largest
                largest = largest.next
            comparisions -= 1
        iterations -= 1


nn1 = Node(4)
nn2 = Node(3)
nn3 = Node(5)
nn4 = Node(1)

linkedlist = LinkedList()
linkedlist.insert(nn1)
linkedlist.insert(nn2)
linkedlist.insert(nn3)
linkedlist.insert(nn4)

linkedlist.display()
print('----------')
sort(linkedlist)
linkedlist.display()
