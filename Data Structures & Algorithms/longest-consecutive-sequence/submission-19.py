class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        st = set(nums)
        res = 0
        count = 1
        for i in st:
            if i - 1 not in st:
                k = i
                while k + 1 in st:
                    count += 1
                    k += 1
            else:
                res = max(res, count)
                count = 1
            res = max(res, count)
        return res