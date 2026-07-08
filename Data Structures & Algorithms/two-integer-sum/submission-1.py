class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target and i!= k:
                    out.extend([i, k])
        return out