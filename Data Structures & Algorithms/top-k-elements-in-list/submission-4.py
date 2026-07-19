class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        emp_dict = {}
        for n in nums:
            emp_dict[n] = emp_dict.setdefault(n, 0) + 1
        sorted_list = sorted(emp_dict.items(), key = lambda x: x[1], reverse = True)
        return [item[0] for item in sorted_list[:k]][:: -1]