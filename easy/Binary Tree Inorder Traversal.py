#question link : https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.l=[]
        def recur(root):
            if root is None:
                return 
            recur(root.left)
            self.l.append(root.val)
            recur(root.right)
        recur(root)
        return self.l
