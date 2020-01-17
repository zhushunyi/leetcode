# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def one(self, root):
        if not root:
            return True
        return root.val == 0 and self.one(root.left) and self.one(root.right)


    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root or self.one(root):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root
