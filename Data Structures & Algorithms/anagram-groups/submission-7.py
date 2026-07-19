class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empt_dict = {}
        for word in strs: 
            sorted_word = "".join(sorted(word))    #time complexity of shorted is m*logm where m is maximum length of word
            if sorted_word not in empt_dict:
                empt_dict[sorted_word] =  [word]
            else:
                empt_dict[sorted_word].append(word)
        return list(empt_dict.values())
# total timme complexity will be n*m*logm