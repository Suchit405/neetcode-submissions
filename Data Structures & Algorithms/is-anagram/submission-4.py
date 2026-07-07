class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        if len(s) != len(t):
            return False
        for a in s:
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1
        for b in t:
            if b in countt:
                countt[b] += 1
            else:
                countt[b] = 1
        for i in s:
            if counts[i] != countt.get(i, 0):
                return False
        return True
        