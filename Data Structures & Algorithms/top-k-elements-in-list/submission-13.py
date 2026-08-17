class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        lst = [[] for _ in range(len(nums)+1)]
        for ke, v in freq.items():
            lst[v].append(ke)
        res = []
        for p in lst:
            if p != []:
                for num in p:
                    res.append(num)
        return res[-k:]
