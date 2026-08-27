class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        h = rows * cols - 1

        while l <= h:
            mid = (l + h) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False