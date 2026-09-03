class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            currsum = 0
            subarray_count = 1
            for i in nums:
                currsum += i
                if currsum > largest:
                    subarray_count += 1
                    currsum = i
            if subarray_count <= k:
                return True
            return False
        l, r = max(nums), sum(nums)
        res = 0
        while r >= l:
            mid = (l + r) // 2
            if cansplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
#This solution uses Binary search on answers