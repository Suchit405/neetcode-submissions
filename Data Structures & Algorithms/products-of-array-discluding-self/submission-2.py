class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[0] = nums[0]
            else:
                prefix[i] = prefix[i - 1]* nums[i]
            j = len(nums) - i - 1
            
            if j == len(nums) - 1:
                suffix[j] = nums[j]
            else:
                suffix[j] = suffix[j+1] * nums[j]
        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * suffix[i + 1]
        return res