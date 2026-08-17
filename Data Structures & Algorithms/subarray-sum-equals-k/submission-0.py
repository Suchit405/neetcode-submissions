class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        count = 0
        currsum = 0
        for n in nums:
            prefix[currsum] = prefix.get(currsum, 0) + 1
            currsum += n
            if currsum - k in prefix:
                count += prefix[currsum - k]
        return count
