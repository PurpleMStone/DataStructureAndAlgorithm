from linked_list_func import *
from utils import *


def unit_test_merge_two_lists():
    """
    测试合并两个升序链表
    """
    list1 = input("please enter list one: ")
    list2 = input("please enter list two: ")

    list1 = [int(ele) for ele in list1.split(" ")]
    list2 = [int(ele) for ele in list2.split(" ")]

    list1 = from_array_to_linked_list(list1)
    list2 = from_array_to_linked_list(list2)

    merged_list = mergeTwoLists(list1, list2)
    print(from_linked_list_to_array(merged_list))


def unit_test_merge_k_lists():
    """
    测试合并K个升序列表
    """
    listNum = int(input("number of lists: "))
    linked_lists = []

    for i in range(listNum):
        temp_list = input("please enter list " + str(i) + ": ")
        temp_list = [int(ele) for ele in temp_list.split(" ")]
        temp_list = from_array_to_linked_list(temp_list)
        linked_lists.append(temp_list)

    merged_list = mergeKLists(linked_lists)
    print(from_linked_list_to_array(merged_list))


def unit_test_remove_nth_from_end():
    """
    测试删除倒数第N个节点
    """
    linked_list = input("please enter linked list: ")
    linked_list = [int(ele) for ele in linked_list.split(" ")]
    linked_list = from_array_to_linked_list(linked_list)

    new_linked_list = removeNthFromEnd(linked_list, 3)
    print(from_linked_list_to_array(new_linked_list))


def unit_test_middle_node():
    """
    测试寻找单链表中间节点
    """
    linked_list = input("please enter linked list: ")
    linked_list = [int(ele) for ele in linked_list.split(" ")]
    linked_list = from_array_to_linked_list(linked_list)

    new_linked_list = middleNode(linked_list)
    print(from_linked_list_to_array(new_linked_list))


def unit_test_has_cycle():
    """
    测试链表是否有环
    """
    linked_list = input("please enter linked list: ")
    linked_list = [int(ele) for ele in linked_list.split(" ")]

    test_cases = []
    # has cycle
    test_cases.append(from_array_to_linked_list_has_cycle(linked_list, 4))
    test_cases.append(from_array_to_linked_list_has_cycle(linked_list, 2))

    # no cycle
    test_cases.append(from_array_to_linked_list_has_cycle(linked_list, -1))

    for test_case in test_cases:
        print(hasCycle(test_case))


def unit_test_detect_cycle():
    """
    测试链表是否有环
    """
    linked_list = input("please enter linked list: ")
    linked_list = [int(ele) for ele in linked_list.split(" ")]

    test_cases = []
    # has cycle
    test_cases.append(from_array_to_linked_list_has_cycle(linked_list, 4))
    test_cases.append(from_array_to_linked_list_has_cycle(linked_list, 2))

    # no cycle
    test_cases.append(from_array_to_linked_list_has_cycle(linked_list, -1))

    for test_case in test_cases:
        node = detectCycle(test_case)
        if node:
            print(node.val)
        else:
            print("no cycle")


unit_test_has_cycle()
unit_test_detect_cycle()
