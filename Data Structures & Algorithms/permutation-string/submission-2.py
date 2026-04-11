class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = defaultdict(int)
        counts2 = defaultdict(int)

        for c in s1:
            counts[c] += 1
        has = 0
        need = len(counts.keys())
        
        l = 0
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                if counts2[s2[l]] == counts[s2[l]]:
                    has -= 1
                counts2[s2[l]] -= 1
                l += 1
            counts2[s2[r]] += 1
            if counts2[s2[r]] == counts[s2[r]]:
                has += 1
            if has == need:
                return True 

        return False
