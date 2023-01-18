from main import Node, LinkedList


def swap_nodes(linkedlist, data1, data2):
    #    # 4 -> 3 -> 5 -> 2 -> 7 -> 1 || 4 -> 7 -> 5 -> 2 -> 3 -> 1
    current = linkedlist.head
    previous = None
    while True:
        if current.data == data1:
            firstNode = current
            break
        previous = current
        current = current.next

    current = linkedlist.head
    while True:
        previousSeond = current
        current = current.next


n1 = Node(4)
n2 = Node(3)
n3 = Node(5)
n4 = Node(2)
n5 = Node(7)
n6 = Node(1)

linkedlist = LinkedList()
linkedlist.insert(n1)
linkedlist.insert(n2)
linkedlist.insert(n3)
linkedlist.insert(n4)
linkedlist.insert(n5)
linkedlist.insert(n6)

linkedlist.display()
swap_nodes(linkedlist, 3, 7)
