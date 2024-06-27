class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d={}
        for i in range(1,len(edges)+2):
            d[i]=0
        for i in edges:
            for j in i:
                d[j]=d[j]+1
        for k,v in d.items():
            if v==len(edges):
                return k
        