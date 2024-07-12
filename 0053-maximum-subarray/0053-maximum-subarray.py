class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0 for i in range(2)]
        dp[0]=nums[0]
        s=nums[0]
        ans=nums[0]
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums),1):
            dp[i%2]=max(dp[(i-1)%2],0)+nums[i]
            ans=max(ans,dp[i%2])
        return ans
        