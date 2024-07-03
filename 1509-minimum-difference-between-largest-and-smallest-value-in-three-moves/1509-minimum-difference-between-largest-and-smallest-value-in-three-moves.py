class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=3:
            return 0
        l=nums[0]
        ans=float('inf')
        ans=min(ans,nums[-4]-nums[0])
        ans=min(ans,nums[-3]-nums[1])
        ans=min(ans,nums[-2]-nums[2])
        ans=min(ans,nums[-1]-nums[3])
        return ans