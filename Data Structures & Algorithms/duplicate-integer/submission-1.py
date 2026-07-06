class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            if nums[i] in nums[i+1:]:
                return True
        return False