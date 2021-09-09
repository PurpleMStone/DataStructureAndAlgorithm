from list_node import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    leetcode 21: 合并两个升序链表
    """
    p1 = l1
    p2 = l2

    # 哨兵节点，简化代码
    dummy = ListNode(0)
    pnew = dummy

    # 每次取p1和p2的较小者接入新链表
    while p1 and p2:
        if p1.val < p2.val:
            pnew.next = p1
            p1 = p1.next
        else:
            pnew.next = p2
            p2 = p2.next
        pnew = pnew.next

    # 仅有p1不为None
    if p1:
        pnew.next = p1

    # 仅有p2不为None
    elif p2:
        pnew.next = p2

    return dummy.next


def mergeKLists(lists: list[ListNode]) -> ListNode:
    import heapq

    if not lists:
        return None

    heap = []
    # 把列表里的所有不为None的链表的头节点的值存入堆中
    # 以值对比大小，i是为了标记特定链表
    for i, linkedlist in enumerate(lists):
        if linkedlist:
            heapq.heappush(heap, (linkedlist.val, i))

    newLinkedList = ListNode(0)
    p = newLinkedList
    while heap:
        # 弹出堆顶元素，将对应节点放入新链表中
        _, i = heapq.heappop(heap)
        p.next = lists[i]

        # 该节点所在的那条链表，指针指向下一节点，存入小顶堆
        if lists[i].next:
            lists[i] = lists[i].next
            heapq.heappush(heap, (lists[i].val, i))

        p = p.next

    return newLinkedList.next
