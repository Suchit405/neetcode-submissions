class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # NOT l, r = 0, max(piles) as eating speed of 0 is invalid and will result zero division error down the road in Binary search algo
        res = 0
        while r >= l:
            k = (l + r) // 2 #NOT k = l + r // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res  #This type of questions are called binary search on answer