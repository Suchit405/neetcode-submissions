class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l, r = 0, 0
        prefix = 1
        res = 0
        for r in range(len(nums)):
            prefix *= nums[r]
            while prefix >= k:
                prefix /= nums[l]
                l += 1
            res += r - l + 1
        return res