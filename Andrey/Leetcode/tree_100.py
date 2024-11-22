"""
100. Same Tree
https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=tree
"""
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have
the same value.

We can can recursevly check each tree and compare them by comparing 
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    state = True
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        self.state = True
        if self.check_recursevely(p, q, True) == False:
            return False
        return self.state
    def check_recursevely(self, p, q, state):
        if self.state == False:
            return False

        if (p == None and q != None) or (p != None and q == None):
            self.state = False
            return False

        if p.val != q.val:
            self.state = False
            return False
        if p.left != q.left and q.left == None:
            self.state = False
            return False
        if p.right != q.right and q.right == None:
            self.state = False
            return False

        if p.left != None or q.left != None:
            self.check_recursevely(p.left, q.left, state)
        
        if p.right != None or q.right != None:
            
            self.check_recursevely(p.right, q.right, state)

if __name__ == '__main__':
    s = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    print(s.isSameTree(p, q))