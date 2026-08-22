class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map_t = {}
        hash_map_s = {}
        res = ""
        for i in t:
            hash_map_t[i] = hash_map_t.get(i, 0) + 1
        need = len(t)
        have = 0
        l = 0
        for r in range(len(s)):
            if s[r] in t:
                hash_map_s[s[r]] = hash_map_s.get(s[r], 0) + 1
                if hash_map_s[s[r]] <= hash_map_t[s[r]]:
                    have += 1
            while need == have:
                if r - l + 1 < len(res) or res == "":
                    res = s[l: r+1]
                if s[l] in t:
                    if hash_map_s[s[l]] <= hash_map_t[s[l]]:
                        have -= 1
                    hash_map_s[s[l]] = hash_map_s[s[l]] - 1
                l += 1
        return res