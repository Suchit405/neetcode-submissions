class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices) - 1):
            for k in range(i+1, len(prices)):
                diff= max(prices[k] - prices[i], diff)
        return diff #This is brute force so time complexity will be O(n^2)