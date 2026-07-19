class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empt_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            empt_dict.setdefault(sorted_word, []).append(word)
        return list(empt_dict.values())