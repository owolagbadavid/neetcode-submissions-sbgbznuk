class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return 1
            
            res = 0

            if s[i] == '0':
                return res
            res += dfs(i+1)
            if i+2 <= len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            dp[i] = res
            return dp[i]

        return dfs(0)