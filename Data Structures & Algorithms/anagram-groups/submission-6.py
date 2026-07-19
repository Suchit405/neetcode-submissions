class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empt_dict = {}
        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s) - ord("a")] += 1               #ord("a") = 81 ord("82") , gives ASIIC values
            empt_dict.setdefault(tuple(count), []).append(word)  #lists are mutable but a dictionary key should be immutable so we need to convert the list to tuple to make it immutable
        return list(empt_dict.values())                         #the output is accepted in form of list only so I converted it to list