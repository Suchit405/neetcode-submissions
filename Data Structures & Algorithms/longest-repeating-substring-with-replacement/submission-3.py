class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        frq = {}
        for r in range(len(s)):
            frq[s[r]] =  frq.get(s[r], 0) + 1
            while r - l + 1 - max(frq.values()) > k:
                frq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res  # These are sliding window questions