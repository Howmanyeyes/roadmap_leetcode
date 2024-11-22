"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=problem-list-v2&envId=tree&difficulty=EASY
"""

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Впервые решаю деревья, поэтому лучший подход я не знаю. Но интуитивно кажется, что нужно написать
ф-цию которая будет рекувно вызывать себя и записывать в глобальную переменную список значений
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res: list[int] = []
    seen: set[TreeNode] = {}
    def inorderTraversal(self, root) -> list[int]:
        self.iter_node(root)
        return self.res
    def iter_node(self, node):
        if node == None:
            return
        if node.val == None:
            return
        if node.left != None:
            self.iter_node(node.left)
        if node not in self.seen:
            self.res.append(node.val)
            self.seen.add(node)
        if node.right != None:
            self.iter_node(node.right)



if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(4)
    print(s.inorderTraversal(root))