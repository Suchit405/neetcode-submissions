from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        monotonic_stack = deque()
        l = 0
        for r in range(len(nums)):
            while monotonic_stack and nums[r] > monotonic_stack[-1]:
                monotonic_stack.pop()
            monotonic_stack.append(nums[r])
            if r == l + (k - 1):
                res.append(monotonic_stack[0])
                if nums[l] == monotonic_stack[0]:
                    monotonic_stack.popleft()
                l += 1
        return res