class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target != target // 1:
            return False
        
        cache = {}

        def dfs(i, n):
            if (i,n) in cache:
                return cache[(i,n)]
            if n == 0:
                return True
            if i >= len(nums):
                return False
            
            cache[(i,n)] = dfs(i+1, n-nums[i]) or dfs(i+1, n)
            return cache[(i,n)]
        return dfs(0, target)
