class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = dict(sorted(zip(position, speed))[::-1]) #OR car = dict(sorted(zip(position, speed), reverse = True))
        stack = []
        for i in car:
            time = (target - i)/car[i]
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
        return len(stack)