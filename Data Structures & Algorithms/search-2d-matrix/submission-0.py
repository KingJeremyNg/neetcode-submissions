class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftRow = 0
        rightRow = len(matrix) - 1
        row = -1

        leftCol = 0
        rightCol = len(matrix[0]) - 1

        while leftRow <= rightRow:
            middle = (leftRow + rightRow) // 2
            if matrix[middle][0] < target and matrix[middle][-1] > target:
                row = middle
                break
            elif matrix[middle][0] == target or matrix[middle][-1] == target:
                return True
            elif matrix[middle][0] > target:
                rightRow = middle - 1
            elif matrix[middle][-1] < target:
                leftRow = middle + 1
        
        while leftCol <= rightCol:
            middle = (leftCol + rightCol) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                rightCol = middle - 1
            elif matrix[row][middle] < target:
                leftCol = middle + 1

        return False
