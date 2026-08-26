class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        position_time = {}
        for i in range(len(speed)):
            distance = target - position[i]
            position_time[position[i]] = distance/speed[i]
        sorted_by_position = dict(sorted(position_time.items(), reverse = True))
        for p in sorted_by_position:
            while stack and sorted_by_position[p] <= sorted_by_position[stack[-1]]:
                sorted_by_position[p] = sorted_by_position[stack[-1]] #This was a quick fix by me to fix issue of the comparing to the previos cas position's time to the current one instead it should have check for the time of the fleet's first car. 
                stack.pop()
            stack.append(p)
        return len(stack)