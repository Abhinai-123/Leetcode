class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i in range(len(edges)+1)]
        rank=[1 for i in range(len(edges)+1)]
        def find(v):
            p=par[v]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        def union(n1,n2):
            i,j=find(n1),find(n2)
            if i==j:
                return False

            if rank[i]>rank[j]:
                par[j]=i
                rank[i]=rank[i]+1
            else:
                par[i]=j
                rank[j]=rank[j]+1
            return True
        for n1,n2 in edges:
                if not union(n1,n2):
                    return [n1,n2]
                
        