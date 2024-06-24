class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        c=0
        q=deque()
        for i in range(len(nums)):
            while q and i > (q[0]+k)-1:
                q.popleft()
            if (nums[i]+len(q))%2==0:
                if i+k>len(nums):
                    return -1
                c=c+1
                q.append(i)
        return c
    
                        
                    
        