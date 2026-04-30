class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = defaultdict(int)

        for h in hand:
            count[h] += 1
        
        hand.sort()
        i = 0
        while i < len(hand):
            if count[hand[i]]:
                nextt = hand[i]
            else:
                i+=1
                continue
            cur = 0
            while True:
                if count[nextt] == 0:
                    return False
                count[nextt] -= 1
                cur += 1
                nextt += 1
                if cur == groupSize:
                    break;
    
        return True