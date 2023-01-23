from main import Node, LinkedList


def remove(linkedlist):
    current_node = linkedlist.head
    while True:
        if current_node.data == current_node.next.data:
            duplicate_node = current_node.next
            current_node.next = duplicate_node.next
            duplicate_node.next = None
            del duplicate_node
            break
        current_node = current_node.next


nn1 = Node(1)
nn2 = Node(2)
nn3 = Node(3)
nn4 = Node(3)
nn5 = Node(5)

linkedlist = LinkedList()
linkedlist.insert(nn1)
linkedlist.insert(nn2)
linkedlist.insert(nn3)
linkedlist.insert(nn4)
linkedlist.insert(nn5)
linkedlist.display()

print('----------------')

remove(linkedlist)
linkedlist.display()
