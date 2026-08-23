class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")" : "(", "}" : "{", "]" : "["}
        a = []
        for i in s:
            if i in hash_map and len(a) > 0:
                if a[-1] == hash_map[i]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        if len(a) == 0:
            return True
        return False