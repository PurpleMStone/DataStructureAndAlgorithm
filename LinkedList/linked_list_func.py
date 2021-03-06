import heapq
from list_node import ListNode

# ------------------------- 1. 合并链表 ---------------------------


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
    """
    leetcode 23: 合并K个升序链表
    """
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

# ------------------------- 2. 寻找链表特定位置节点 ---------------------------


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    leetcode 19: 删除链表的倒数第 N 个结点
    """
    dummy = ListNode(0)
    dummy.next = head

    fast, slow = dummy, dummy

    # fast指针先走n步
    while n:
        fast = fast.next
        n -= 1

    # 快慢指针一起走
    while fast.next:
        fast = fast.next
        slow = slow.next

    # 删除倒数第n个节点
    slow.next = slow.next.next

    return dummy.next


def middleNode(head: ListNode) -> ListNode:
    """
    leetcode 876. 链表的中间结点
    """
    slow, fast = head, head

    while fast and fast.next:
        # 快指针走两步
        fast = fast.next.next

        # 慢指针走一步
        slow = slow.next

    return slow

# ------------------------- 3. 环形链表 ---------------------------


def hasCycle(head: ListNode) -> bool:
    """
    leetcode 141: 判断链表是否有环
    """
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False


def detectCycle(head: ListNode) -> ListNode:
    """
    leetcode 142: 返回链表开始入环的第一个节点
    """
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        # 链表有环，slow从head开始，fast从相遇点开始
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # 快慢指针再次相遇的地方就是环的入口
            return slow

    # 链表无环
    return None

# ------------------------- 4. 相交链表 ---------------------------


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    """
    leetcode 160: 相交链表
    """
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1


# ------------------------- 5. 反转链表 ---------------------------
def reverseList_recur(head: ListNode) -> ListNode:
    """
    leetcode 206: 反转链表-递归方法
    """
    if head == None:
        return None

    if head.next == None:
        return head

    newHead = reverseList_recur(head.next)
    head.next.next = head
    head.next = None

    return newHead


def reverseList_iter(head: ListNode) -> ListNode:
    """
    leetcode 206: 反转链表-迭代方法
    """
    pre = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    return pre


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    """
    leetcode 92: 反转某区间的链表
    """
    global successor
    successor = None

    def reverseN(head, count):

        global successor
        if count == 1:
            successor = head.next
            return head

        newhead = reverseN(head.next, count - 1)
        head.next.next = head
        head.next = successor

        return newhead

    if left == 1:
        return reverseN(head, right)
    head.next = reverseBetween(head.next, left - 1, right - 1)
    return head


def isPalindrome(head: ListNode) -> bool:
    """
    leetcode 234: 判断是否是回文链表
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    # 左半部分从头开始
    left = head
    # 右半部分反转链表
    right = reverseList_iter(slow)

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
