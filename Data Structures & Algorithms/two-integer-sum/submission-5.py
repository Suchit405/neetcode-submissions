class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            a  = target - nums[i]
            if a in nums[i+1:] and (nums[i+1:].index(a)+i+1) != i:
                out.extend([i, (nums[i+1:].index(a)+i+1)])
        return out