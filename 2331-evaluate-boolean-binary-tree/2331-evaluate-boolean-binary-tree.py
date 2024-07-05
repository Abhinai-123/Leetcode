# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def solve(n):
            if not n:
                return 0
            if n.val==0 or n.val==1:
                return n.val==1
            l=solve(n.left)
            r=solve(n.right)
            if n.val==2:
                return l or r
            elif n.val==3:
                return l and r
            return False
        return solve(root)
            