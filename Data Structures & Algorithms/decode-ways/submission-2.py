class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        first = 1
        second = 0 if s[n - 1] == '0' else 1

        for i in range(n - 2, -1, -1):
            tmp = second
            if s[i] == '0':
                second = 0
                first = tmp
                continue

            one = second

            two = 0
            two_digit = int(s[i:i+2])
            if 10 <= two_digit <= 26:
                two = first

            second = one + two
            first = tmp

        return second