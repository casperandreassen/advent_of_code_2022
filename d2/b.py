import os

# lose, win, draw
scores = {'A': [1, 'Z', 'Y', 'X'], 'B': [2, 'X', 'Z', 'Y'], 'C': [3, 'Y', 'X', 'Z'], 'X': 1, 'Y': 2, 'Z': 3}
score = 0

with open (os.getcwd() + "/d2/input.txt") as input:
    for game in input:
        plays = game.rstrip().split(' ')
        if plays[1] == 'X':
            score += scores[scores[plays[0]][1]]
        elif plays[1] == 'Y':
            score += scores[scores[plays[0]][3]] + 3
        else:
            score += scores[scores[plays[0]][2]] + 6


print(f'You got a score of {score}')