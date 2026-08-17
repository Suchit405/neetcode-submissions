class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mp = {}
        res = []
        for n, m in enumerate(nums):
            mp[m] = n
        for i in range(len(nums)):
            target = 0 - nums[i]
            for r in range(i+1, len(nums)):
                if target - nums[r] in mp and mp[target - nums[r]] > r :
                    if [nums[i], nums[r], (target - nums[r])] not in res:
                        res.append([nums[i], nums[r], (target - nums[r])])
        return res 