class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
        feq = [[] for i in range(len(nums) + 1)]
        for n, c in hash_map.items():
            feq[c].append(n)
        res = []
        for n in feq:
            if n != []:
                for q in n:
                    res.append(q)
        return res[-k:]