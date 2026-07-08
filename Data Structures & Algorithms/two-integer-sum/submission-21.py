class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        m = len(nums)
        for i in range(m):
            for k in range(i+1, m):
                if nums[i] + nums[k] == target and i!= k:
                    out.extend([i, k])
        return out