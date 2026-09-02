class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = nums[0]
        maxsum = nums[0]
        for i in nums[1:]:
            currmax = max(i, currmax + i)
            maxsum = max(maxsum, currmax)
        return maxsum