from main import Node, LinkedList


# 1 -> 3 -> 4 || 2 -> 7 -> 9
# 1 -> 2 -> 3 -> 4 -> 7 -> 9

def merge(first_list, second_list, merge_list):
    current_first = first_list.head
    current_second = second_list.head
    while True:
        if current_first is None:
            merge_list.insert(current_second)
            break
        if current_second is None:
            merge_list.insert(current_first)
            break
        if current_first.data < current_second.data:
            current_first_next = current_first.next
            current_first.next = None
            merge_list.insert(current_first)
            current_first = current_first_next
        else:
            current_second_next = current_second.next
            current_second.next = None
            merge_list.insert(current_second)
            current_second = current_second_next


nn1 = Node(1)
nn2 = Node(3)
nn3 = Node(4)

nn4 = Node(2)
nn5 = Node(7)
nn6 = Node(9)

linkedlist1 = LinkedList()
linkedlist2 = LinkedList()
merge_list = LinkedList()

linkedlist1.insert(nn1)
linkedlist1.insert(nn2)
linkedlist1.insert(nn3)

linkedlist2.insert(nn4)
linkedlist2.insert(nn5)
linkedlist2.insert(nn6)

linkedlist1.display()
print('---------')
linkedlist2.display()

merge(linkedlist1, linkedlist2, merge_list)

print('---------')
merge_list.display()
