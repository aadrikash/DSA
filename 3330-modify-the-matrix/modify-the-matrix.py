class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])

        for j in range(cols):

            maximum = matrix[0][j]

            for i in range(rows):
                maximum = max(maximum , matrix[i][j])

            for i in range(rows):
                if matrix[i][j] == -1:
                    matrix[i][j]  = maximum 
        return matrix
        