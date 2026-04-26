class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = maxSub = nums[0]
        for i in range(1, len(nums)):
            cur = max(0, cur)
            cur += nums[i]
            maxSub = max(maxSub, cur)
        return maxSub