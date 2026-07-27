class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for k in strs:
            s += str(len(k)) + '#' + k
        return s

    def decode(self, s: str) -> List[str]:
        final = []
        count = 0
        d = 0
        while count < len(s):
            if s[count] == '#':
                length = int(s[count - d : count])
                final.append(s[count + 1 : count + length + 1])
                count += length + 1
                d = 0
            else:
                count += 1
                d += 1
        return final