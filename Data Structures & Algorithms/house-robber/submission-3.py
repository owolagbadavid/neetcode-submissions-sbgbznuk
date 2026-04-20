class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0, 0]

        for i in range(n-1, -1, -1):
            tmp = dp[0]
            dp[0] = max(nums[i]+dp[1], dp[0])
            dp[1] = tmp
        return dp[0]
