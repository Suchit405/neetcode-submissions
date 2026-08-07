class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        new_set = set(nums)
        lengths = []
        for i in new_set:
            if i - 1 not in new_set: #checking an element in an list is of time complexity of O(n) and checking an element in set is of time complexity O(1) as it uses Hashed table and hash(value) is used to store the value so the python exactly knows if it exists. Same goes for dictionary in python it uses hash table to time complexity is O(n).
                length = 1
                while i + 1 in new_set:
                    i += 1
                    length += 1
                lengths.append(length)
        return max(lengths)
        