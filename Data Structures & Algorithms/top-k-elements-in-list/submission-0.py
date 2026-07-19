class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        emp_dict = {}
        for n in nums:
            emp_dict[n] = emp_dict.setdefault(n, 0) + 1
        sorted_dict = sorted(emp_dict.items(), key = lambda x: x[1])
        oup = []
        d = k
        while d >= 1:
            oup.append(sorted_dict[-d][0])
            d -= 1
        return oup