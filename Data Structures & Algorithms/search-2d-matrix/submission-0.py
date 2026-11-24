class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for this problem, we're going to need to apply binary search twice; 
        # once on row and again on column (once we know which row.)
        ROWS, COLS = len(matrix), len(matrix[0])
        lower_values, higher_values = 0, ROWS - 1
    
        while lower_values <= higher_values:
            # note rollover risk on large values; not a problem with our constraints
            midpoint = (lower_values + higher_values) // 2
            # case 1: target < matrix[m][0]; exclude higher_values rows
            if target < matrix[midpoint][0]:
                higher_values = midpoint - 1
            # case 2: target > matrix[m][-1]; exclude lower_values rows
            elif target > matrix[midpoint][-1]:
                lower_values = midpoint + 1
            # we have the correct row
            else:
                break

        # failed to find relevant row
        if not lower_values <= higher_values:
            return False

        row = (lower_values + higher_values) // 2
        left, right = 0, COLS - 1

        # note: Binary search _must_ be <=; this tripped me up.
        while left <= right:
            mid = (right + left) // 2
            # case 1: target > midpoint; exclude left side
            if target > matrix[row][mid]:
                left = mid + 1
            # case 2: target < midpoint; exclude right side
            elif target < matrix[row][mid]:
                right = mid - 1
            # target found
            else:
                return True

        return False
        