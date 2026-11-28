class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # b search the rows themselves
        # then b search again within the rows

        row_l, row_r = 0, len(matrix) - 1

        while row_l <= row_r:
            row_m = row_l + (row_r - row_l) // 2

            if target < matrix[row_m][0]:
                row_r = row_m - 1
            elif target > matrix[row_m][-1]:
                row_l = row_m + 1
            else:
                l, r = 0, len(matrix[row_m]) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    val = matrix[row_m][m]
                    if target < val:
                        r = m - 1
                    elif target > val:
                        l = m + 1
                    else:
                        return True
                return False

        return False
