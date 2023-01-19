from main import Node, LinkedList


def sort(linkedlist):
    # iterations depend on no. of nodes
    iterations = linkedlist.list_length() - 1
    while iterations != 0:
        iterations -= 1
        break


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
