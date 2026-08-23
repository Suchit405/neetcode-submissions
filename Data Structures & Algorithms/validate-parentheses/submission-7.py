class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")" : "(", "}" : "{", "]" : "[" }
        a = []
        for i in s:
            if i in [")","]","}"]:
                if len(a) == 0: 
                    return False
                s = a.pop()
                if s != hash_map[i]:
                    return False
            else:
                a.append(i)
        if len(a) != 0:
            return False
        return True