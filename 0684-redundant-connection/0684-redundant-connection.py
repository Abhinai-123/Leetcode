class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds=[i for i in range(len(edges)+1)]
        rank=[1 for i in range(len(edges)+1)]
        def findparent(v):
            p=ds[v]
            while p!=ds[p]:
                ds[p]=ds[ds[p]]
                p=ds[p]
            return p
        for i,j in edges:
            p1=findparent(i)
            p2=findparent(j)
            if p1==p2:
                return [i,j]
            if rank[p1]<rank[p2]:
                ds[p1]=p2
                rank[p2]+=1
            elif rank[p1]>rank[p2]:
                ds[p2]=p1
                rank[p1]+=1
            else:
                ds[p2]=p1
                rank[p1]+=1
        
        