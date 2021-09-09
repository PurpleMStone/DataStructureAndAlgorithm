from list_node import ListNode


def from_array_to_linked_list(arr):
    linked_list = []

    for i, ele in enumerate(arr):
        linked_list.append(ListNode(ele))

    for i in range(len(linked_list) - 1):
        linked_list[i].next = linked_list[i + 1]

    return linked_list[0]


def from_linked_list_to_array(head):
    p = head
    arr = []
    while p:
        arr.append(p.val)
        p = p.next
    return arr
