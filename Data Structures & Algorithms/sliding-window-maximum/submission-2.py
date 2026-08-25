from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonic_stack = deque([])
        res = [0] * len(nums)
        l, r = len(nums) - 1, len(nums) - 1
        while l >= 0:
            while monotonic_stack and nums[l] >= nums[monotonic_stack[-1]]:
                monotonic_stack.pop()
            monotonic_stack.append(l)
            if l == r - k + 1:
                res[r] = nums[monotonic_stack[0]] if monotonic_stack else nums[l]
                if monotonic_stack and monotonic_stack[0] == r:
                    monotonic_stack.popleft()
                r -= 1
            l -= 1
        return res[k - 1:]