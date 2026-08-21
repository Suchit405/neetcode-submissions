class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_id = [0] * 26
        s2_id = [0] * 26
        l, r = 0, 0
        for i in s1:
            s1_id[ord(i) - ord("a")] += 1
        while r < len(s2):
            s2_id[ord(s2[r]) - ord("a")] += 1
            while r - l + 1 > len(s1):
                s2_id[ord(s2[l]) - ord("a")] -= 1                
                l += 1
            r += 1
            if s1_id == s2_id:
                return True
        return False
