# Example 1
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

from typing import List

def Searcha2DMatrix(matrix: List[List[int]], target: int) -> bool:
    row_l = 0
    row_r = len(matrix) - 1
    row_m = 0

    while row_l <= row_r:
        row_m = row_l + (row_r-row_l)//2
        if target < matrix[row_m][0]:
            row_r = row_m - 1
        elif target > matrix[row_m][-1]:
            row_l = row_m + 1
        else:
            break
    
    if row_l < 0 or row_r > len(matrix) - 1:
        return False

    col_l = 0
    col_r = len(matrix[row_m]) - 1
    col_m = 0

    while col_l <= col_r:
        col_m = col_l + (col_r - col_l)//2
        if target < matrix[row_m][col_m]:
            col_r = col_m - 1
        elif target > matrix[row_m][col_m]:
            col_l = col_m + 1
        else:
            return True
    return False

# Testing

test1_matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
test1_target = 3
test1_expected = True
test1_actual = Searcha2DMatrix(test1_matrix, test1_target)

assert test1_actual == test1_expected, f"Test 1 is expected to be {test1_expected} but is actually {test1_actual}."

test2_matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
test2_target = 3
test2_expected = True
test2_actual = Searcha2DMatrix(test2_matrix, test2_target)

assert test2_actual == test2_expected, f"Test 2 is expected to be {test2_expected} but is actually {test2_actual}."
