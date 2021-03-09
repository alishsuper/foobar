def solution(n):
    # your code here
    size = n + 1

    matrix = [[0 for _ in range(size)] for _ in range(size)]

    matrix[0][0] = 1
    for prev in range(1, size):
        for left in range(0, size):
            matrix[prev][left] = matrix[prev - 1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev - 1][left - prev]
    print(matrix)
    return matrix[n][n] - 1