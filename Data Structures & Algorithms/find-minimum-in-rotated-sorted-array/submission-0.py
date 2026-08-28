class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while r >= l:
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[-1] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1