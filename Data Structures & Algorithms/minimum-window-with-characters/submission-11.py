class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_id = [0] * 126
        s_id = [0] * 126 
        res = ""
        for i in t:
            t_id[ord(i)] += 1
        need  = len(t)
        have = 0
        l = 0
        for r in range(len(s)):
            s_id[ord(s[r])] += 1
            if s_id[ord(s[r])] <= t_id[ord(s[r])]:
                have += 1
            while need == have:
                if r - l + 1 < len(res) or res == "":
                    res = s[l: r+1]
                if s_id[ord(s[l])] <= t_id[ord(s[l])]:
                    have -= 1
                s_id[ord(s[l])] -= 1
                l += 1
        return res