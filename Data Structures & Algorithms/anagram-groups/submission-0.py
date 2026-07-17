class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empt_dict = {}
        out = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in empt_dict:
                empt_dict[sorted_word] =  [word]
            else:
                empt_dict[sorted_word].append(word)
        for ls in empt_dict.values():
            out.append(ls)
        return out
