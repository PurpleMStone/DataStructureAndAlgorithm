class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def remove(head):
    res = head.val
    head = head.next
    return head, res


def addFirst(head, val):
    new_node = LinkedList(val)
    new_node.next = head
    head = new_node
    return head


def get(self):
    return self.val
