class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r >= l:
            mid = (l + r) // 2 #OR mid = l + (r-l) // 2 to avoid over flow in other languages like C++ and java byt, not needed in python not l + r // 2 due to BODMAS rule
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1