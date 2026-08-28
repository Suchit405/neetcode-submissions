class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while r >= l:
            mid  = (l + r) // 2
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[r]:
                res = min(res, nums[mid])
                r = mid - 1
        return res