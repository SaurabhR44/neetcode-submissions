# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.checklrheight(root.left)
        right = self.checklrheight(root.right)
        if abs(left-right) >1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    


    def checklrheight(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.checklrheight(root.left),self.checklrheight(root.right))