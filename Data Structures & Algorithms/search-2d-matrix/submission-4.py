class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1
        while r >= l:
            mid = (l + r) // 2
            i = mid // n
            if matrix[i][(mid % n)] == target:
                return True
            elif target >= matrix[i][(mid % n)]:
                l = mid + 1
            else:
                r = mid - 1
        return False