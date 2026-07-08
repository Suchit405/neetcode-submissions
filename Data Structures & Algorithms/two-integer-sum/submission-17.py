class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            a  = target - nums[i]
            t = nums[i+1:]
            if a in t:
                out.extend([i, (nums[i+1:].index(a)+i+1)])
        return out