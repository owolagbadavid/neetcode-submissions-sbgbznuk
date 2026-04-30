class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        groups = len(hand) // groupSize

        count = defaultdict(int)

        for h in hand:
            count[h] += 1
        
        hand.sort()
        i = 0
        while i < len(hand):
            if count[hand[i]]:
                res = []
                next = hand[i]
            else:
                i+=1
                continue
            cur = 0
            while True:
                if (res and res[-1]+1 != next) or count[next] == 0:
                    return False
                res.append(next)
                count[next] -= 1
                cur += 1
                next += 1
                if cur == groupSize:
                    break;
    
        return True