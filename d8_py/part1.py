import os

matrix = []
visible = 0

with open (os.getcwd() + "/d8_py/input.txt") as input:
    for i, line in enumerate(input):
        matrix.append([])
        for c in line.rstrip():
            matrix[i].append(int(c))

    # Calculate visible trees
    for i in range(len(matrix)):
        for n in range(len(matrix)):
            if (n == 0 or n == (len(matrix[i]) - 1) or i == 0):
                visible += 1
                continue
            check = matrix[i][n]
            # Top
            num = 0
            for c in range(i - 1, -1, -1):
                if matrix[c][n] < check:
                    num += 1
            if num == i:
                visible += 1
                continue

            # Right
            num = 0
            for c in range(n + 1, len(matrix[i])):
                if matrix[i][c] < check:
                    num += 1
            if num == len(matrix[i]) - (n + 1):
                visible += 1
                continue

            # Bottom
            num = 0
            for c in range(i + 1, len(matrix)):
                if matrix[c][n] < check:
                    num += 1
            if num == len(matrix) - (i + 1):
                visible += 1
                continue

            # Left
            num = 0
            for c in range(n - 1, -1, -1):
                if matrix[i][c] < check:
                    num += 1
            if num == n:
                visible += 1
                continue


print(visible)