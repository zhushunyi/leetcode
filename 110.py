# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left),self.height(node.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right))<2