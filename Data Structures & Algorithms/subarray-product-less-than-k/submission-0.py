class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        l, r = 0, 0
        prefix = 1
        res = 0
        for r in range(len(nums)):
            prefix *= nums[r]
            if prefix < k:
                res += r - l + 1
            while prefix >= k and l < r:
                prefix /= nums[l]
                l += 1
                if prefix < k:
                    res += r - l + 1
        return res