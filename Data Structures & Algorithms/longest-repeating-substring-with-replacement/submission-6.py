class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        frq = {}
        mx = 0
        for r in range(len(s)):
            frq[s[r]] =  frq.get(s[r], 0) + 1
            mx = max(frq[s[r]], mx)
            while r - l + 1 - mx > k:
                frq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res  # These are sliding window questions