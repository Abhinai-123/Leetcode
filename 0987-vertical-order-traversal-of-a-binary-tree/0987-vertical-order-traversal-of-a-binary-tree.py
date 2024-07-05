# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        mi = float("inf")
        ma = float("-inf")

        def solve(node, level, depth):
            nonlocal mi, ma
            if not node:
                return
            d[level].append((depth, node.val))
            mi = min(mi, level)
            ma = max(ma, level)
            solve(node.left, level - 1, depth + 1)
            solve(node.right, level + 1, depth + 1)

        solve(root, 0, 0)
        ans = []
        for i in range(mi, ma + 1):
            ans.append([val for depth, val in sorted(d[i])])
        return ans
