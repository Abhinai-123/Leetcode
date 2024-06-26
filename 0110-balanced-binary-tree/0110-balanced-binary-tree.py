# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(n):
            l=0
            r=0
            if not n:
                return 0
            if not n.left and not n.right:
                return 1
            else:
                l=check(n.left)
                r=check(n.right)
                if l==-1 or r==-1 or abs(l-r)>1:
                    return -1
                return 1+max(l,r)
        if check(root)==-1:
            return False
        else:
            return True