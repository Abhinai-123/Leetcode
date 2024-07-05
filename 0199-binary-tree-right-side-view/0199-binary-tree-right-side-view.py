# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        q=[[root]]
        ans=[]
        while(q):
            n=q.pop(0)
            t=[]
            p=[]
            for i in n:
                if i:
                    p.append(i.val)
                    t.append(i.left)
                    t.append(i.right)
            if t:
                q.append(t)
            if p:
                ans.append(p[-1])
        return ans
        