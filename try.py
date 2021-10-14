"""
求正三角数组的最大路径和
"""


class TreeNode:
    def __init__(self, val=0, index=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.index = index


memo = dict()


def maxSum(root):
    if not root:
        return 0

    if str(root.index) in memo:
        print(str(root.index))
        return memo[str(root.index)]

    max_sum = root.val + max(maxSum(root.left), maxSum(root.right))
    memo[str(root.index)] = max_sum
    return max_sum


node1 = TreeNode(7, 0)
node2 = TreeNode(3, 1)
node3 = TreeNode(8, 2)
node1.left, node1.right = node2, node3

node4 = TreeNode(8, 3)
node5 = TreeNode(1, 4)
node6 = TreeNode(0, 5)
node2.left, node2.right = node4, node5
node3.left, node3.right = node5, node6

node7 = TreeNode(2, 6)
node8 = TreeNode(7, 7)
node9 = TreeNode(4, 8)
node10 = TreeNode(4, 9)
node4.left, node4.right = node7, node8
node5.left, node5.right = node8, node9
node6.left, node6.right = node9, node10

node11 = TreeNode(4, 10)
node12 = TreeNode(5, 11)
node13 = TreeNode(2, 12)
node14 = TreeNode(6, 13)
node15 = TreeNode(5, 14)
node7.left, node7.right = node11, node12
node8.left, node8.right = node12, node13
node9.left, node9.right = node13, node14
node10.left, node10.right = node14, node15

print(maxSum(node1))
