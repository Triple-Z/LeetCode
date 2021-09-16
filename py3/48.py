class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # horizontal turn-over
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        # transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]