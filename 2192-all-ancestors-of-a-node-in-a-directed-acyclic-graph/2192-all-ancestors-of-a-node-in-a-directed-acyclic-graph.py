from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for frm, to in edges:
            graph[to].append(frm)
        
        def dfs(node):
            if ancestors[node] is not None:
                return ancestors[node]
            ancestors[node] = set()
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            return ancestors[node]
        
        ancestors = [None] * n
        for i in range(n):
            if ancestors[i] is None:
                dfs(i)
        
        answer = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return answer
