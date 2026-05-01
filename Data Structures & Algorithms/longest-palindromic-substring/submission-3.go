func longestPalindrome(s string) string {
    res := string(s[0])

    expand := func(l int, r int) {
        for l >= 0 && r < len(s) && s[l] == s[r] {
            cur := s[l:r+1]
            if len(cur) > len(res) {
                res = cur
            }
            l -= 1
            r += 1
        }
    }

    for i := range s{
        l := i - 1
        r := i + 1
        expand(l, r)
        l = i
        r = i+1
        expand(l, r)
    }
    return res
}
