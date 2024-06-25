class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        d=[j[0] for j in jobs]
        p=[j[1] for j in jobs]
        mp=[]
        q=0
        for i in p:
            q=max(q,i)
            mp.append(q)
        x=len(d)-1
        ans=0
        def solve(i):
            lo=0
            hi=x
            s=0
            while(lo<=hi):
                mid=(lo+hi)//2
                if d[mid]<=i:
                    lo=mid+1
                elif d[mid]>i:
                    hi=mid-1
            if hi>=0:
                    s=mp[hi]
            return s
        for i in worker:
            ans=ans+solve(i)
        return ans
        