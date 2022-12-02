import os

scores = {'A': [1, 'Y', 'X'], 'B': [2, 'Z', 'Y'], 'C': [3, 'X', 'Z'], 'X': 1, 'Y': 2, 'Z': 3}
score = 0

with open (os.getcwd() + "/d2/input.txt") as input:
    for game in input:
        plays = game.rstrip().split(' ')
        if scores[plays[0]][1] == plays[1]:
            score += scores[plays[1]] + 6
        elif scores[plays[0]][1] != plays[1] and scores[plays[0]][2] != plays[1]:
            score += scores[plays[1]]
        else:
            score += scores[plays[1]] + 3

print(f'You got a score of {score}')