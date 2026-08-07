class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        new_set = set(nums)
        lengths = []
        for i in new_set:
            if i - 1 not in new_set:
                length = 1
                while i + 1 in new_set:
                    i += 1
                    length += 1
                lengths.append(length)
        return max(lengths)
        