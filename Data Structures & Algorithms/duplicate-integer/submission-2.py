class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed_set = set()
        for i in nums:
            if i in hashed_set:
                return True
            else:
                hashed_set.add(i)
        return False