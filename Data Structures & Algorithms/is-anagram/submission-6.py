class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        k = len(s)
        p = len(t)
        if k != p:
            return False
        for i in range(k):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)
        for d in counts:
            if counts[d] != countt.get(d, 0):
                return False
        return True