# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes={}
        child=set()
        for i in descriptions:
            p,c,b=i
            if p not in nodes:
                nodes[p]=TreeNode(p)
            if c not in nodes:
                nodes[c]=TreeNode(c)
            if b:
                nodes[p].left=nodes[c]
            else:
                nodes[p].right=nodes[c]
            child.add(c)
        for p,q,r in descriptions:
            if p not in child:
                return nodes[p]
        
        