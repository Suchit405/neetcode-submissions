class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lss = [0] * 26
        lst = [0] * 26
        for i in s:
            lss[ord("a") - ord(i)] += 1
        for i in t:
            lst[ord("a") - ord(i)] += 1
        return lss == lst