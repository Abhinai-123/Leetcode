class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=[]
        for i in range(1,n+1,1):
            q.append(i)
        ind=0
        while(len(q)>1):
            ind=(ind+k-1)%len(q)
            q.pop(ind)
        return q[0]