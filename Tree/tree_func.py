from tree_node import TreeNode
from utils import *


def flatten(self, root: TreeNode) -> None:
    """
    leetcode 114: 二叉树展开为链表
    """
    if not root:
        return

    # 展平左右子树
    self.flatten(root.left)
    self.flatten(root.right)

    # 保存右子树
    right = root.right

    root.right = root.left
    root.left = None

    p = root
    while p.right:
        p = p.right

    # 将展开的右子树接到单链表的末尾
    p.right = right


def constructMaximumBinaryTree(nums: list[int]) -> TreeNode:
    """
    leetcode 654: 最大二叉树
    """

    if not len(nums):
        return None

    max_val, max_index = maxNum(nums)
    root = TreeNode(max_val)

    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index+1:])

    return root


def buildTreePreIn(self, preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    leetcode 105: 从前序与中序遍历序列构造二叉树
    """
    if not len(preorder) or not len(inorder):
        return

    root_val = preorder[0]
    root = TreeNode(root_val)

    # 找到中序遍历中的根节点所在的位置
    root_in_i = inorder.index(root_val)
    # 获取左子树包含的节点个数
    left_size = root_in_i

    root.left = self.buildTree(preorder[1:left_size+1], inorder[:root_in_i])
    root.right = self.buildTree(preorder[left_size+1:], inorder[root_in_i+1:])

    return root


def buildTreeInPost(self, inorder: list[int], postorder: list[int]) -> TreeNode:
    """
    leetcode 106: 从中序与后序遍历序列构造二叉树
    """
    if not len(inorder) or not len(postorder):
        return

    root_val = postorder[-1]
    root = TreeNode(root_val)

    # 找到中序遍历中的根节点所在的位置
    root_in_i = inorder.index(root_val)
    # 获取左子树包含的节点个数
    left_size = root_in_i

    root.left = self.buildTree(inorder[:root_in_i], postorder[:left_size])
    root.right = self.buildTree(
        inorder[root_in_i+1:], postorder[left_size:-1])
    return root


def findDuplicateSubtrees(root: TreeNode) -> list[TreeNode]:
    """
    leetcode 652: 寻找重复的子树
    """
    # 1.序列化子树
    # 2.将子树存入字典，统计出现的次数
    # 3.出现次数大于1的存入结果列表中
    res = []
    dict_subtree = {}

    def traverse(root: TreeNode) -> str:
        if not root:
            return "#"

        left = traverse(root.left)
        right = traverse(root.right)

        subTree = left + "," + right + "," + str(root.val)

        if subTree in dict_subtree:
            if dict_subtree[subTree] == 1:
                res.append(root)
            dict_subtree[subTree] += 1

        else:
            dict_subtree[subTree] = 1

        return subTree

    traverse(root)
    return res


def sequense(root: TreeNode) -> str:
    if not root:
        return "#"
    left = sequense(root.left)
    right = sequense(root.right)
    seq = left + "," + right + "," + str(root.val)
    return seq


def convertBST(root: TreeNode) -> TreeNode:
    """
    leetcode 538: 把二叉搜索树转换为累加树
    """
    global count
    count = 0

    def traverse(root: TreeNode) -> None:
        if not root:
            return
        traverse(root.right)
        global count
        count += root.val
        root.val = count
        traverse(root.left)

    traverse(root)
    return root


def countNodes(root: TreeNode) -> int:
    """
    leetcode 222: 完全二叉树的节点个数
    """
    if not root:
        return 0

    hl, hr = 0, 0
    l, r = root, root
    while l:
        l = l.left
        hl += 1
    while r:
        r = r.right
        hr += 1

    # 满二叉树
    if hl == hr:
        return pow(2, hl) - 1

    # 普通二叉树
    return countNodes(root.left) + countNodes(root.right) + 1
