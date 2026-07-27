class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp_withoutzero = 1
        zero_count = 0
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                temp_withoutzero *= nums[i]
        for j in range(len(nums)):
            if zero_count == 0:
                res.append(temp_withoutzero // nums[j])
            if zero_count == 1: 
                if nums[j] == 0:
                    res.append(temp_withoutzero)
                else:
                    res.append(0)
            if zero_count >= 2:
                res.append(0)

        return res