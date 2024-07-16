# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def solve(n,ans,v):
            if not n:
                return 
            if n.val==v:
                return ans
            ans.append("L")
            l=solve(n.left,ans,v)
            if l:
                return ans
            ans.pop()
            ans.append("R")
            r=solve(n.right,ans,v)
            if r:
                return ans
            ans.pop()
            return 
        p=solve(root,[],startValue)
        q=solve(root,[],destValue)
        i=0
        d=[]

        while(i<len(p) and i<len(q)):
            if p[i]==q[i]:
                i=i+1
            else:
                break
        for j in range(i,len(p),1):
            d.append("U")
        for j in range(i,len(q),1):
            d.append(q[j])
        return "".join(d)