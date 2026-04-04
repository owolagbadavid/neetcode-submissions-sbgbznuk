class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [[0]*2 for _ in strs]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if strs[i][j] == '0':
                    count[i][0] += 1
                else:
                    count[i][1] += 1
        
        dp = defaultdict(int)

        for zeros, ones in count:
            for M in range(m, zeros-1, -1):
                for N in range(n, ones-1, -1):
                    dp[(M,N)] = max(1+dp[(M-zeros,N-ones)], dp[(M,N)])
        
        return dp[(m,n)]