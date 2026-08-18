class Solution:
    def trap(self, height: List[int]) -> int:
        lft_mx = [0] * len(height)
        rt_mx = [0] * len(height)
        lf = 0
        rt = 0
        total = 0
        r = len(height) - 1
        for l in range(len(height)):
            lf = max(lf, height[l])
            rt = max(rt, height[r - l])
            lft_mx[l] = lf
            rt_mx[r - l] = rt
        for i in range(len(height)):
            temp_sm = min(lft_mx[i], rt_mx[i]) - height[i]
            if temp_sm > 0:
                total += temp_sm
        return total
