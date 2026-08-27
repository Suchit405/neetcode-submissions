class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = dict(sorted(zip(position, speed))[::-1]) #OR car = dict(sorted(zip(position, speed), reverse = True))
        res = 0
        last_time = 0
        for i in car:
            time = (target - i)/car[i]
            if time > last_time:
                res += 1
                last_time = time
        return res #This solution does not ueses Stack but I shoul also look for the previous Stack solution that I did