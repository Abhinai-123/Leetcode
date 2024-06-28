class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edges=[0 for i in range(n)]
        for i in roads:
            edges[i[0]] +=1
            edges[i[1]] +=1
        res=0
        co=1
        edges.sort()
        for i in edges:
            res+=co*i
            co=co+1
        return res
        