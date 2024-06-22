class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans=float("-inf")
        position.sort()
        def check(mi,m):
            c=1
            p=position[0]
            for i in range(1,len(position),1):
                if (position[i]-p)>=mi:
                    c=c+1
                    p=position[i]
            return c>=m
                
        l=1
        h=position[-1]  
        while(l<=h):
            mi=(l+h)//2
            if check(mi,m):
                ans=max(ans,mi)
                l=mi+1
            else:
                h=mi-1
        return ans