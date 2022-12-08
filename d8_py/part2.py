import os

matrix = []
best = 0

with open (os.getcwd() + "/d8_py/input.txt") as input:
    for i, line in enumerate(input):
        matrix.append([])
        for c in line.rstrip():
            matrix[i].append(int(c))

    # Calculate visible trees
    for i in range(len(matrix)):
        for n in range(len(matrix)):
            check = matrix[i][n]
            # Top
            top = 0
            for c in range(i - 1, -1, -1):
                if matrix[c][n] < check:
                    top += 1
                else:
                    top += 1
                    break

            # Right
            right = 0
            for c in range(n + 1, len(matrix[i])):
                if matrix[i][c] < check:
                    right += 1
                else:
                    right += 1
                    break

            # Bottom
            bottom = 0
            for c in range(i + 1, len(matrix)):
                if matrix[c][n] < check:
                    bottom += 1
                else:
                    bottom += 1
                    break


            # Left
            left = 0
            for c in range(n - 1, -1, -1):
                if matrix[i][c] < check:
                    left += 1
                else:
                    left += 1
                    break

            score = top * right * bottom * left
            if score > best:
                best = score


print(best)