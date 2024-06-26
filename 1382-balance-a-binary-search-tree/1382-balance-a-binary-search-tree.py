# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def solve(n,l):
            if not n:
                return
            solve(n.left,l)
            l.append(n.val)
            solve(n.right,l)
        solve(root,l)
        lo=0
        hi=len(l)-1
        def construct(l,lo,hi):
            if lo>hi:
                return None
            m=(lo+hi)//2
            cn=TreeNode(l[m])
            cn.left=construct(l,lo,m-1)
            cn.right=construct(l,m+1,hi)
            return cn
        return construct(l,0,hi)