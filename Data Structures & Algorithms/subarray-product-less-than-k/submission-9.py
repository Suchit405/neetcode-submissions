class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        prefix_product = 1
        res = 0
        for r in range(len(nums)):
            prefix_product *= nums[r]
            if prefix_product < k:
                res += r - l + 1
            while prefix_product >= k and l < r:
                prefix_product /= nums[l]
                l += 1
                if prefix_product < k:
                    res += r - l + 1
        return res