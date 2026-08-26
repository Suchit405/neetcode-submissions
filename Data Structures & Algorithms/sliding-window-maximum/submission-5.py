class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            if r == l + k -1:
                res.append(q[0])
                if q[0] == nums[l] :
                    q.popleft()
                l += 1
        return res