class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [0]
        for i in range(len(prices) - 1):
            for k in range(i+1, len(prices)):
                diff.append(prices[k] - prices[i])
        return max(diff)