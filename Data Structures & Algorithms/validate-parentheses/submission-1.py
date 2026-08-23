class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")" : "(", "}" : "{", "]" : "[" }
        a = []
        x = ""
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
        
        #     if len(a) > 0:
        #         if a[-1] == hash_map[i]:
        #             a.pop()
        #     a.append(i)
        # if len(a) == 0:
        #     return True
        # return False