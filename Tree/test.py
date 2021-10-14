from tree_func import *


def unit_test_find_duplicate_subtrees():
    node1 = TreeNode(1)
    node2, node3 = TreeNode(2), TreeNode(3)
    node1.left, node1.right = node2, node3

    node4 = TreeNode(4)
    node2.left = node4

    node5, node6 = TreeNode(2), TreeNode(4)
    node3.left, node3.right = node5, node6

    node7 = TreeNode(4)
    node5.left = node7

    list_subtree = findDuplicateSubtrees(node1)
    list_subtree = [sequense(ele) for ele in list_subtree]
    print(list_subtree)


def unit_test_convert_BST():
    node1 = TreeNode(4)
    node2, node3 = TreeNode(1), TreeNode(6)
    node1.left,  node1.right = node2, node3

    node4, node5 = TreeNode(0), TreeNode(2)
    node2.left, node2.right = node4, node5

    node6, node7 = TreeNode(5), TreeNode(7)
    node3.left, node3.right = node6, node7

    node8 = TreeNode(3)
    node5.right = node8

    node9 = TreeNode(8)
    node7.right = node9

    print(sequense(convertBST(node1)))


unit_test_convert_BST()
