class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monotonic_stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while monotonic_stack and temperatures[i] >= temperatures[monotonic_stack[-1]]:
                monotonic_stack.pop()
            res[i] = (monotonic_stack[-1] - i) if monotonic_stack else 0
            monotonic_stack.append(i)
        return res
