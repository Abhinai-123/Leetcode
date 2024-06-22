class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        co=0
        n=len(grumpy)
        for i in range(n):
            if grumpy[i]==0:
                co=co+customers[i]
        s=0
        for i in range(minutes):
            if grumpy[i]==1:
                s=s+customers[i]
        ml=co+s
        i=0
        j=minutes   
        while(i<=j and j<n):
            if grumpy[i]==1:
                s=s-customers[i]
            if grumpy[j]==1:
                s=s+customers[j]
            
            ml=max(ml,co+s)
            i=i+1
            j=j+1
        return ml
            
            
        