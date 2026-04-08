class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2:
            return False

        target = total // 2
        
        dp = [[False]*(target+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, target+1):
                skip = dp[i-1][j] 
                if j - nums[i] >= 0:
                    dp[i][j] = skip or dp[i-1][j - nums[i]]

        return dp[n-1][target]
