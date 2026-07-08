class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            a  = target - nums[i]
            rest = nums[i+1:]
            if a in rest:
                out.extend([i, (rest.index(a)+i+1)])
        return out