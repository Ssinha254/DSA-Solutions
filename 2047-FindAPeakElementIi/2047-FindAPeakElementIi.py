# Last updated: 4/21/2026, 11:24:21 PM
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        left, right = 0, n - 1 
        while left <= right:
            mid = (left + right) // 2

            max_row = 0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            is_left_smaller = mid == 0 or mat[max_row][mid] > mat[max_row][mid - 1]
            is_right_smaller = mid == n - 1 or mat[max_row][mid] > mat[max_row][mid + 1]

            if is_left_smaller and is_right_smaller:
                return [max_row, mid]

            if mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]:
                right = mid - 1
            else:
                left = mid + 1