# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def solve(n,s):
            if not n:
                return s
            r=solve(n.right,s)
            n.val=n.val+r
            s=n.val
            l=solve(n.left,s)
            return l
        solve(root,0)
        return root
        