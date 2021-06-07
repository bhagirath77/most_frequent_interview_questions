# question link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def recur(root,h):
            if not root:
                return h
            if not root.right:
                return recur(root.left,h+1)
            if not root.left:
                return recur(root.right,h+1)
            return (max(recur(root.left,h+1),recur(root.right,h+1)))
        x=recur(root,0)
        return x
