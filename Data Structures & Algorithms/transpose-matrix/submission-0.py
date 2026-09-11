class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        matrix_transpose = []
        for i in range(col):
            matrix_transpose.append([0] * row)

        for i in range(row):
            for j in range(col):
                matrix_transpose[j][i] = matrix[i][j]

        return matrix_transpose