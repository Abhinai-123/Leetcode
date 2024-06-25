# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def solve(n,s):
            if n:
                print("n.val",n.val)
                print("sum",s)
            if not n:
                print("from retrun",s)
                return s
            print("right")
            r=solve(n.right,s)
            n.val=n.val+r
            s=n.val
            print("left")
            l=solve(n.left,s)
            print(f"n.val{n.val}")
            print(s)
            return l
        solve(root,0)
        return root
        